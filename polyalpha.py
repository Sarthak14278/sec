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
