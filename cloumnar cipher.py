# Input plaintext and key
pText = input('Enter your message: ')
key = input('Enter your key: ')

def encryption(pText, key):
    num_columns = len(key)
    columns = [''] * num_columns

    # Fill columns with characters from plaintext
    for index, char in enumerate(pText):
        column_index = index % num_columns
        columns[column_index] += char

    # Pair key characters with their corresponding columns
    paired_columns = list(zip(key, columns))

    # Sort the columns based on the key
    sorted_columns = sorted(paired_columns)

    # Combine columns in sorted order to create ciphertext
    cText = ''.join([column[1] for column in sorted_columns])
    return cText

# Encrypt plaintext using the key
cText = encryption(pText, key)
print("Cipher text is: " + cText)

#Decrypt
import math

# Function to decrypt Columnar Transposition Cipher
def columnar_decrypt(ciphertext, key):
    # Determine the number of columns
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)
    
    # Create a list of empty strings to store the columns
    columns = [''] * num_columns
    
    # Create a list of positions for the columns based on the key order
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    column_positions = [item[0] for item in sorted_key]
    
    # Fill in the columns with the ciphertext
    ciphertext_idx = 0
    for col in column_positions:
        for row in range(num_rows):
            if ciphertext_idx < len(ciphertext):
                columns[col] += ciphertext[ciphertext_idx]
                ciphertext_idx += 1
    
    # Reconstruct the plaintext by reading across the rows
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_columns):
            if row < len(columns[col]):
                plaintext += columns[col][row]
    
    return plaintext

# Example usage
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

decrypted_text = columnar_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
