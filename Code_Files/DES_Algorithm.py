from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def get_user_input():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the 8-byte security key (in hex format, e.g., 12345678): ")
    return plaintext, bytes.fromhex(key)

def encrypt_des(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC)
    plaintext_bytes = plaintext.encode('utf-8')
    padded_plaintext = pad(plaintext_bytes, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return cipher.iv, ciphertext

def decrypt_des(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext_bytes = unpad(padded_plaintext, DES.block_size)
    return plaintext_bytes.decode('utf-8')

def main():
    plaintext, key = get_user_input()
    
    # Ensure the key is 8 bytes long
    if len(key) != 8:
        print("Error: Key must be 8 bytes long.")
        return
    
    iv, ciphertext = encrypt_des(plaintext, key)
    decrypted_text = decrypt_des(ciphertext, key, iv)
    
    print(f"Original Plaintext: {plaintext}")
    print(f"Encrypted Text (hex): {binascii.hexlify(ciphertext).decode('utf-8')}")
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
