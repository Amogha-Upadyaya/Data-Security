# This program aims to encrypt the inputted word/statement via Caesar Cipher
# Program:

# 1. Ask user to input the word/statement
text = input("Enter text to encrypt: ")
# 2. Ask user to input the shift value
shift = int(input("Enter shift value: "))
# 3. Encrypt the word/statement via Caesar Cipher
encrypted_text = ""
for char in text:
    if char.isalpha():
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26)
        else:
            encrypted_text += chr((ord(char) + shift - 97) % 26)
    else:
        encrypted_text += char

# 4. Display the encrypted word/statement
print("Encrypted text: ", encrypted_text)