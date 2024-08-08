from Crypto.Cipher import DES
from Crypto import Random

def pad(text):
    """Pads the text to a multiple of 8 bytes."""
    return text + (b' ' * (8 - len(text) % 8))

def encrypt(key, plaintext):
    """Encrypts the plaintext using DES in ECB mode."""
    key = key.encode('ascii')
    plaintext = pad(plaintext.encode('ascii'))
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(plaintext)

def decrypt(key, ciphertext):
    """Decrypts the ciphertext using DES in ECB mode."""
    key = key.encode('ascii')
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(ciphertext).rstrip()

def main():
    key = input("Enter the encryption key (8 characters): ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt(key, plaintext)
    print("Encrypted text:", ciphertext)

    decrypted_text = decrypt(key, ciphertext).decode('ascii')
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
