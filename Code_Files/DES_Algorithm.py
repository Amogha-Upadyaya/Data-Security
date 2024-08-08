import numpy as np

# Permutation and Substitution Tables (simplified for demonstration)
# Actual DES tables are much more complex and defined in DES standard

# Initial Permutation (IP) table
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

# Final Permutation (IP-1) table
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

# Define the key schedule
def key_schedule(key):
    # This function should generate 16 sub-keys from the main key.
    # For demonstration purposes, we're using a fixed sub-key here.
    return [key] * 16

# Feistel function (simplified)
def feistel_function(right_half, sub_key):
    return right_half ^ sub_key  # Simplified XOR operation for demonstration

# DES encryption function
def des_encrypt(plaintext, key):
    # Initial Permutation
    permuted_text = np.array([plaintext[i - 1] for i in IP])
    
    # Split into left and right halves
    left_half = permuted_text[:32]
    right_half = permuted_text[32:]
    
    sub_keys = key_schedule(key)
    
    for i in range(16):
        # Feistel function
        temp = feistel_function(right_half, sub_keys[i])
        
        # Swap halves
        left_half, right_half = right_half, left_half ^ temp
    
    # Combine halves and apply final permutation
    combined = np.concatenate([left_half, right_half])
    ciphertext = np.array([combined[i - 1] for i in IP_INV])
    
    return ciphertext

# DES decryption function (inverse of encryption)
def des_decrypt(ciphertext, key):
    # Initial Permutation
    permuted_text = np.array([ciphertext[i - 1] for i in IP])
    
    # Split into left and right halves
    left_half = permuted_text[:32]
    right_half = permuted_text[32:]
    
    sub_keys = key_schedule(key)[::-1]  # Reverse the key schedule for decryption
    
    for i in range(16):
        # Feistel function
        temp = feistel_function(right_half, sub_keys[i])
        
        # Swap halves
        left_half, right_half = right_half, left_half ^ temp
    
    # Combine halves and apply final permutation
    combined = np.concatenate([left_half, right_half])
    plaintext = np.array([combined[i - 1] for i in IP_INV])
    
    return plaintext

# Example usage
if __name__ == "__main__":
    key = np.random.randint(0, 2, size=64)  # 64-bit key
    plaintext = np.random.randint(0, 2, size=64)  # 64-bit plaintext

    ciphertext = des_encrypt(plaintext, key)
    decrypted_text = des_decrypt(ciphertext, key)

    print("Plaintext: ", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted:", decrypted_text)
