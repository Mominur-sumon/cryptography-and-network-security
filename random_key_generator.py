import random
import string

def generate_identical_key_files(filename1, filename2, length):
    # Generate a random uppercase key
    key = ''.join(random.choices(string.ascii_uppercase, k=length))
    
    # Write the same key to both files
    with open(filename1, 'w') as f1, open(filename2, 'w') as f2:
        f1.write(key)
        f2.write(key)
    
    print(f"Identical random key of length {length} saved to '{filename1}' and '{filename2}'.")

# Example usage
generate_identical_key_files("encrypt_key.txt", "decrypt_key.txt", 1000000)
