import numpy as np

# Padding function
def pad(text):
    pad_len = 8 - (len(text) % 8)
    return text + chr(pad_len) * pad_len

# Unpadding function
def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

# Convert string to binary representation
def string_to_bin_array(s):
    bin_array = []
    for char in s:
        bin_value = bin(ord(char))[2:].zfill(8)  # Convert each character to an 8-bit binary
        bin_array.extend([int(bit) for bit in bin_value])
    return np.array(bin_array)

# Convert binary array to string
def bin_array_to_string(bin_array):
    chars = []
    for i in range(0, len(bin_array), 8):
        byte = bin_array[i:i+8]
        byte_str = ''.join(str(bit) for bit in byte)
        chars.append(chr(int(byte_str, 2)))
    return ''.join(chars)

# ... (IP, IP_INV, key_schedule, feistel_function, des_encrypt, des_decrypt)

if __name__ == "__main__":
    # Get user input for plaintext and key
    plaintext_input = input("Enter the plaintext: ")
    key_input = input("Enter the key (at least 8 characters): ")
    
    # Pad the plaintext input
    padded_plaintext_input = pad(plaintext_input)
    
    # Convert to binary arrays
    plaintext = string_to_bin_array(padded_plaintext_input)[:64]  # Use only the first 64 bits for simplicity
    key = string_to_bin_array(key_input)[:64]  # Use only the first 64 bits for simplicity
    
    # Pad if needed
    while len(plaintext) < 64:
        plaintext = np.append(plaintext, 0)
    while len(key) < 64:
        key = np.append(key, 0)

    # Encrypt and Decrypt
    ciphertext = des_encrypt(plaintext, key)
    decrypted_text = des_decrypt(ciphertext, key)

    # Convert back to string
    decrypted_message = bin_array_to_string(decrypted_text)

    # Unpad the decrypted message
    unpadded_decrypted_message = unpad(decrypted_message)

    print("Plaintext: ", plaintext_input)
    print("Ciphertext:", ''.join(map(str, ciphertext)))
    print("Decrypted:", unpadded_decrypted_message.strip())
