import rsa

def main():
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter another prime number q: "))
    
    try:
        pub_key, priv_key = rsa.generate_rsa_keys(p, q)
    except ValueError as e:
        print(e)
        return
    
    print("Public Key: ", pub_key)
    print("Private Key: ", priv_key)
    
    message = input("Enter a message to encrypt: ")
    encrypted_message = rsa.encrypt(message, pub_key)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = rsa.decrypt(encrypted_message, priv_key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
