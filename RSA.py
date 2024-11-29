import random
from math import gcd

# Function to generate a random prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(start, end):
    while True:
        prime = random.randint(start, end)
        if is_prime(prime):
            return prime

# RSA key generation
def generate_rsa_keys():
    # Generate two large prime numbers
    p = generate_prime(100, 300)  # Small range for demonstration; increase for security
    q = generate_prime(100, 300)
    while p == q:
        q = generate_prime(100, 300)
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Compute d such that (d * e) % phi = 1
    d = pow(e, -1, phi)

    # Public key: (e, n), Private key: (d, n)
    return (e, n), (d, n)

# Encryption
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    # Convert plaintext to integers and encrypt
    return [pow(ord(char), e, n) for char in plaintext]

# Decryption
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    # Decrypt ciphertext and convert back to characters
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main program
public_key, private_key = generate_rsa_keys()
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

plaintext = input("Enter the plaintext: ")
ciphertext = rsa_encrypt(plaintext, public_key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = rsa_decrypt(ciphertext, private_key)
print(f"Decrypted text: {decrypted_text}")
