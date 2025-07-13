
import os

def read_and_consume_key(filename, length):
    with open(filename, 'r') as f:
        key = f.read().strip()
    
    if len(key) < length:
        raise ValueError(f"{filename} does not contain enough characters.")
    
    used_key = key[:length]
    remaining_key = key[length:]

    # Overwrite file with remaining key
    with open(filename, 'w') as f:
        f.write(remaining_key)

    return used_key


def otp_encrypt(plaintext, key):
    ciphertext = ''
    for p, k in zip(plaintext, key):
        if p == ' ':
            ciphertext += ' '
        else:
            p_val = ord(p) - ord('A') + 1  # A = 1, ..., Z = 26
            k_val = ord(k) - ord('A') + 1
            c_val = (p_val + k_val) % 26
            if c_val == 0:
                c_val = 26
            ciphertext += chr(c_val + ord('A') - 1)
    return ciphertext

def otp_decrypt(ciphertext, key):
    plaintext = ''
    for c, k in zip(ciphertext, key):
        if c == ' ':
            plaintext += ' '
        else:
            c_val = ord(c) - ord('A') + 1
            k_val = ord(k) - ord('A') + 1
            p_val = (c_val - k_val + 26) % 26
            if p_val == 0:
                p_val = 26
            plaintext += chr(p_val + ord('A') - 1)
    return plaintext

# === Example Usage ===
if __name__ == "__main__":
    # plaintext = "UNIVERSITY OF RAJSHAHI BD"  
    plaintext = "XYZ"  
    encrypt_key = read_and_consume_key("encrypt_key.txt", len(plaintext))

    print("Plaintext: ", plaintext)
    print("Key Used:  ", encrypt_key)

    decrypt_key = read_and_consume_key("decrypt_key.txt", len(plaintext))
    cipher = otp_encrypt(plaintext, encrypt_key)
    print("Ciphertext:", cipher)

    recovered = otp_decrypt(cipher, decrypt_key)
    print("Recovered: ", recovered)