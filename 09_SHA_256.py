import hashlib

def sha256_hash(text):
    # Encode the text into bytes
    encoded_text = text.encode()

    # Create a SHA-256 hash object
    sha256_obj = hashlib.sha256()

    # Update the hash object with the encoded text
    sha256_obj.update(encoded_text)

    # Get the hexadecimal digest
    hash_hex = sha256_obj.hexdigest()

    return hash_hex

# Example usage
if __name__ == "__main__":
    input_text = "12548888gjv fg fggghh"
    print("Input:", input_text)
    print("SHA-256 Hash:", sha256_hash(input_text))
