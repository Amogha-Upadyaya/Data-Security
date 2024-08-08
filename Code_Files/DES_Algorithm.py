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

# Permutation and Substitution Tables (simplified for demonstration)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def key_schedule(key):
    sub_keys = [key[:32] for _ in range(16)]  # Truncate to 32 bits for simplicity
    return sub_keys

def feistel_function(right_half, sub_key):
    return right_half ^ sub_key  # Simplified XOR operation for demonstration

def des_encrypt(plaintext, key):
    permuted_text = np.array([plaintext[i - 1] for i in IP])
    left_half = permuted_text[:32]
    right_half = permuted_text[32:]
    sub_keys = key_schedule(key)
    for i in range(16):
        temp = feistel_function(right_half, sub_keys[i])
        left_half, right_half = right_half, left_half ^ temp
    combined = np.concatenate([left_half, right_half])
    ciphertext = np.array([combined[i - 1] for i in IP_INV])
    return ciphertext

def des_decrypt(ciphertext, key):
    permuted_text = np.array([ciphertext[i - 1] for i in IP])
    left_half = permuted_text[:32]
    right_half = permuted_text[32:]
    sub_keys = key_schedule(key)[::-1]
    for i in range(16):
        temp = feistel_function(right_half, sub_keys[i])
        left_half, right_half = right_half, left_half ^ temp
    combined = np.concatenate([left_half, right_half])
    plaintext = np.array([combined[i - 1] for i in IP_INV])
    return plaintext

if __name__ == "__main__":
    # Get user input for plaintext and key
    plaintext_input = input("Enter the plaintext: ")
    key_input = input("Enter the key (at least 8 characters): ")
    
    # Pad the plaintext input
    padded_plaintext_input = pad(plaintext_input)
    
    # Convert to binary arrays
    plaintext = string_to_bin_array(padded_plaintext_input)
    key = string_to_bin_array(key_input)[:64]  # Use only the first 64 bits for simplicity
    
    # Pad key if needed
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
