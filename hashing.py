import hashlib

def hash_text(text):
    """
    Hash a string using multiple algorithms and display the results.

    Parameters:
        text (str): The input text to hash.
    """
    algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    print(f"Text to hash: {text}")
    for algo in algorithms:
        # Create hash object
        hash_object = hashlib.new(algo)
        # Update the hash with the text encoded as bytes
        hash_object.update(text.encode('utf-8'))
        # Print the hexadecimal digest
        print(f"{algo.upper()} hash: {hash_object.hexdigest()}")

# Get input from the user
text = input("Enter the text to hash: ")
hash_text(text)










#MID_SQUARE
def mid_square_hash(key, hash_size):
    """
    Generate a hash value using the Mid-Square Method.
    
    Parameters:
        key (int): The input key to hash (must be an integer).
        hash_size (int): The desired size of the hash table (number of slots).
    
    Returns:
        int: The hash value.
    """
    # Step 1: Square the key
    squared_key = key ** 2
    
    # Step 2: Convert squared_key to string and extract the middle portion
    squared_str = str(squared_key)
    mid_start = len(squared_str) // 2 - 1  # Adjust index for center
    mid_end = mid_start + 2                # Take 2 middle digits
    mid_digits = int(squared_str[mid_start:mid_end])
    
    # Step 3: Modulo to fit hash table size
    return mid_digits % hash_size

# Example usage
key = int(input("Enter the key (integer): "))
hash_size = int(input("Enter the hash table size: "))
hash_value = mid_square_hash(key, hash_size)
print(f"Hash value for key {key} is: {hash_value}")
