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
