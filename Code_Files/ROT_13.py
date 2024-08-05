# Function to perform ROT13 cipher
def rot13(input_string):
    result = ""
    for char in input_string:
        if 'A' <= char <= 'Z':  # Uppercase letters
            new_char = ord(char) + 13
            if new_char > ord('Z'):
                new_char -= 26
            result += chr(new_char)
        elif 'a' <= char <= 'z':  # Lowercase letters
            new_char = ord(char) + 13
            if new_char > ord('z'):
                new_char -= 26
            result += chr(new_char)
        elif '0' <= char <= '9':  # Digits
            new_char = ord(char) + 13
            if new_char > ord('9'):
                new_char -= 10
            result += chr(new_char)
        else:
            result += char  # Special characters remain the same
    return result

# Take an input string from the user
input_string = input("Enter a string to apply ROT13: ")

# Apply ROT13 cipher
rot13_string = rot13(input_string)

# Print the ROT13 ciphered string
print("ROT13 Ciphered string:", rot13_string)
