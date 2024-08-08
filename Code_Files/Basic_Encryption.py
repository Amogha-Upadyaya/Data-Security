# Design the basic encryption and decryption algorithms like caesar cipher, transposition cipher, ROT13 Cipher

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a text using the Caesar cipher.

    Args:
        text: The text to be encrypted or decrypted.
        shift: The number of positions to shift the letters.
        mode: 'encrypt' or 'decrypt'.

    Returns:
        The encrypted or decrypted text.
    """

    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - offset - shift) % 26 + offset)
            else:
                raise ValueError("Invalid mode")
            result += shifted_char
        else:
            result += char  # Preserve spaces and other characters
    return result

def transposition_cipher(text, key):
    """
    Encrypts or decrypts a text using the transposition cipher.

    Args:
        text: The text to be encrypted or decrypted.
        key: The key used for encryption/decryption.

    Returns:
        The encrypted or decrypted text.
    """

    column_count = len(key)
    row_count = (len(text) + column_count - 1) // column_count
    cipher_text = [[''] * column_count for _ in range(row_count)]  # Create a matrix

    index = 0
    for row in range(row_count):
        for col in range(column_count):
            if index < len(text):
                cipher_text[row][col] = text[index]
                index += 1

    ordered_text = ""
    for col_index in key:
        for row in range(row_count):
            if row * column_count + col_index - 1 < len(text):
                ordered_text += cipher_text[row][col_index - 1]

    return ordered_text

def rot13_cipher(text):
    """
    Encrypts or decrypts a text using the ROT13 cipher.

    Args:
        text: The text to be encrypted or decrypted.

    Returns:
        The encrypted or decrypted text.
    """

    return caesar_cipher(text, 13, 'encrypt')

def main():
    text = input("Enter the text: ")
    choice = int(input("Choose an option:\n1. Caesar Cipher\n2. Transposition Cipher\n3. ROT13 Cipher\n"))

    if choice == 1:
        shift = int(input("Enter the shift value: "))
        mode = input("Enter mode (encrypt/decrypt): ")
        result = caesar_cipher(text, shift, mode)
    
    elif choice == 2:
        key = list(map(int, input("Enter the key (column numbers): ").split()))
        result = transposition_cipher(text, key)
    
    elif choice == 3:
        result = rot13_cipher(text)
    
    else:
        print("Invalid choice!")
        return  # Exit the program

    print("Result:", result)

if __name__ == "__main__":
    main()