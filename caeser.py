def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # To handle shifts greater than 26
    if mode.lower() == "decrypt":
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around within alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

# Input from user
text = input("Enter your text: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt? ")

# Perform encryption or decryption
result = caesar_cipher(text, shift, mode)
print(f"Result: {result}")

#decryption
def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    
    for char in ciphertext:
        # Check if the character is a letter
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            # Handle uppercase letters
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            # Non-alphabet characters remain unchanged
            decrypted_text += char
            
    return decrypted_text

# Example usage
ciphertext = input("Enter the ciphertext: ")
key = int(input("Enter the decryption key: "))

decrypted_text = caesar_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
