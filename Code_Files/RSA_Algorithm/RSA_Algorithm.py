import math

# Function to compute the greatest common divisor using the Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

# Function to compute modular inverse
def mod_inverse(e, phi_n):
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % phi_n

# Function to generate RSA keys
def generate_rsa_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q must be prime numbers.")
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = 65537  # Common choice for e
    
    if math.gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime with phi_n.")
    
    d = mod_inverse(e, phi_n)
    
    return (e, n), (d, n)  # Return public and private keys

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to encrypt a message
def encrypt(message, pub_key):
    e, n = pub_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, priv_key):
    d, n = priv_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message
