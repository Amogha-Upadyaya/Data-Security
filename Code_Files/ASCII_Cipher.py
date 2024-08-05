# Function to convert a string to its binary representation
def string_to_binary(input_string):
    binary_string = ""
    for char in input_string:
        ascii_value = ord(char)
        binary_char = ""
        while ascii_value > 0:
            binary_char = str(ascii_value % 2) + binary_char
            ascii_value = ascii_value // 2
        # Pad with leading zeros to make sure each byte is 8 bits long
        while len(binary_char) < 8:
            binary_char = '0' + binary_char
        binary_string += binary_char
    return binary_string

# Function to convert a binary string to ASCII characters
def binary_to_ascii(binary_string):
    ascii_string = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        ascii_value = 0
        for bit in byte:
            ascii_value = (ascii_value << 1) + int(bit)
        ascii_string += chr(ascii_value)
    return ascii_string

# Function to XOR two binary strings
def xor_binary(binary1, binary2):
    xor_result = ""
    for bit1, bit2 in zip(binary1, binary2):
        xor_result += '1' if bit1 != bit2 else '0'
    return xor_result

# Main program
# Take two words as input from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Convert words to binary
binary1 = string_to_binary(word1)
binary2 = string_to_binary(word2)

# Display binary forms
print("Binary form of first word:", binary1)
print("Binary form of second word:", binary2)

# Ensure the binary strings are of the same length by padding the shorter one
max_len = max(len(binary1), len(binary2))
binary1 = binary1.zfill(max_len)
binary2 = binary2.zfill(max_len)

# Perform XOR operation
xor_result = xor_binary(binary1, binary2)

# Convert XOR result to ASCII
ascii_result = binary_to_ascii(xor_result)

# Display XOR result in binary and ASCII
print("XOR result in binary:", xor_result)
print("XOR result in ASCII:", ascii_result)

# Display the plain text
print("Plain text from XOR result:", ascii_result)