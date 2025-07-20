import hashlib

def md5_hash(text):
    # Create MD5 hash object
    hash_object = hashlib.md5()

    # Convert input string to bytes and update the hash object
    hash_object.update(text.encode())

    # Get the hexadecimal digest of the hash
    return hash_object.hexdigest()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter text to hash using MD5: ")
    hash_result = md5_hash(user_input)
    print("MD5 Hash:", hash_result)
