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
