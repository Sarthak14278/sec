def vigenere_cipher(text, key, mode):
    result = []
    key = key.upper()  # Ensure the key is uppercase for consistency
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            char = char.upper()  # Convert to uppercase for processing
            
            # Determine the shift value based on the key
            shift = ord(key[key_index]) - ord('A')
            if mode.lower() == "decrypt":
                shift = -shift  # Reverse shift for decryption
            
            # Apply the shift and wrap around within the alphabet
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char if is_upper else shifted_char.lower())
            
            # Move to the next character in the key
            key_index = (key_index + 1) % key_length
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)

# Input from user
text = input("Enter your text: ")
key = input("Enter your key: ")
mode = input("Encrypt or Decrypt? ")

# Perform encryption or decryption
result = vigenere_cipher(text, key, mode)
print(f"Result: {result}")



#Decrypt
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_index = 0
    
    # Iterate through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the shift based on the key character
            key_char = key[key_index % len(key)].upper()  # Use the key cyclically
            shift = ord(key_char) - ord('A')  # Calculate the shift for this character
            
            # Decrypt for uppercase letters
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            # Decrypt for lowercase letters
            elif char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabet characters remain unchanged
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Example usage
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

decrypted_text = vigenere_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
