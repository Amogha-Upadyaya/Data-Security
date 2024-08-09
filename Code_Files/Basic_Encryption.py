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

def transposition_cipher(text, key, mode):
    """
    Encrypts or decrypts a text using the transposition cipher.

    Args:
        text: The text to be encrypted or decrypted.
        key: The key used for encryption/decryption, a list of column indices.
        mode: 'encrypt' or 'decrypt'.

    Returns:
        The encrypted or decrypted text.
    """
    column_count = len(key)
    row_count = (len(text) + column_count - 1) // column_count

    # Padding text to fit the grid if necessary
    padded_text = text.ljust(row_count * column_count)

    if mode == 'encrypt':
        # Create matrix for encryption
        matrix = [list(padded_text[i * column_count:(i + 1) * column_count]) for i in range(row_count)]

        # Create encrypted text by reading columns in the order specified by the key
        encrypted_text = ""
        for col_index in key:
            for row in matrix:
                if col_index - 1 < len(row):
                    encrypted_text += row[col_index - 1]

        return encrypted_text

    elif mode == 'decrypt':
        # Create matrix for decryption
        matrix = [[''] * column_count for _ in range(row_count)]

        # Fill columns in the order specified by the key
        index = 0
        for col_index in key:
            for row in range(row_count):
                if index < len(text):
                    matrix[row][col_index - 1] = text[index]
                    index += 1

        # Create decrypted text by reading rows
        decrypted_text = ""
        for row in matrix:
            decrypted_text += ''.join(row)

        return decrypted_text.rstrip()  # Remove any padding added during encryption

    else:
        raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")


def rot13_cipher(text, mode='encrypt'):
    """
    Encrypts or decrypts a text using the ROT13 cipher.

    Args:
        text: The text to be encrypted or decrypted.
        mode: 'encrypt' or 'decrypt'. Since ROT13 is symmetric, this is optional.

    Returns:
        The encrypted or decrypted text.
    """
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Invalid mode")

    return caesar_cipher(text, 13, mode)

def main():
    text = input("Enter the text: ")
    choice = int(input("Choose an option:\n1. Caesar Cipher\n2. Transposition Cipher\n3. ROT13 Cipher\n"))

    if choice == 1:
        shift = int(input("Enter the shift value: "))
        mode = input("Enter mode (encrypt/decrypt): ")
        result = caesar_cipher(text, shift, mode)
    
    elif choice == 2:
        key = list(map(int, input("Enter the key (column numbers, e.g., 1 2 3): ").split()))
        mode = input("Enter mode (encrypt/decrypt): ")
        result = transposition_cipher(text, key, mode)
    
    elif choice == 3:
        mode = input("Enter mode (encrypt/decrypt): ")
        result = rot13_cipher(text, mode)
    
    else:
        print("Invalid choice!")
        return  # Exit the program

    print("Result:", result)

if __name__ == "__main__":
    main()
