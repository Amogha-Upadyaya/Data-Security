# Take string "Hi class Of 2022" as plaintext and string "CYBER" as key
PlainText = "Hi Class Of 2022"
Key = "CYBER"

# Convert the plaintext string and key string into their ASCII forms
PlainTextASCII = [ord(char) for char in PlainText]
#print("PlainTextASCII: ", PlainTextASCII)
KeyASCII = [ord(char) for char in Key]
print("KeyASCII: ",KeyASCII)
# Convert the ASCII forms of the plaintext string and key string into binary form
# Perform XOR between the binary forms of the plaintext string and key string.
# If the length of key string is shorter that the length of plain text string, repeat the the same key string for the rest of the plaintext string.
# Proceed to find the ASCII form of the XOR result
# Finally, find the plain text form of the XOR result
# Display the plain text form of the XOR Result

'''
def text_to_ascii(text):
    return [ord(char) for char in text]

def ascii_to_binary(ascii_list):
    return ['{:08b}'.format(char) for char in ascii_list]

def xor_binary(bin1, bin2):
    # XOR two binary strings, assuming they are of the same length
    return ''.join('1' if a != b else '0' for a, b in zip(bin1, bin2))

def binary_to_ascii(binary_str):
    # Convert binary string to ASCII
    return int(binary_str, 2)

def ascii_to_text(ascii_val):
    # Convert ASCII value to text
    return chr(ascii_val)

def encrypt(plaintext, key):
    # Step 1: Convert plaintext and key to ASCII
    plaintext_ascii = text_to_ascii(plaintext)
    key_ascii = text_to_ascii(key)
    
    # Step 2: Convert ASCII to binary
    plaintext_binary = ascii_to_binary(plaintext_ascii)
    key_binary = ascii_to_binary(key_ascii)
    
    # Step 3: Perform XOR, repeating key if necessary
    key_length = len(key_binary)
    ciphertext_binary = ''
    for i, char_bin in enumerate(plaintext_binary):
        key_char_bin = key_binary[i % key_length]
        xor_result = xor_binary(char_bin, key_char_bin)
        ciphertext_binary += xor_result
    
    # Step 4: Convert binary ciphertext back to ASCII and then to text
    ciphertext_ascii = binary_to_ascii(ciphertext_binary)
    ciphertext_text = ascii_to_text(ciphertext_ascii)
    
    return ciphertext_text

# Example usage:
plaintext = "Hi class Of 2022"
key = "CYBER"

encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
'''