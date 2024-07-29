"""
# Take string "Hi class Of 2022" as plaintext and string "CYBER" as key
PlainText = "Hi Class Of 2022"
Key = "CYBER"

# Convert the plaintext string and key string into their ASCII forms
PlainTextASCII = [ord(char) for char in PlainText]
#print("PlainTextASCII: ", PlainTextASCII)
KeyASCII = [ord(char) for char in Key]
#print("KeyASCII: ",KeyASCII)

# Convert the ASCII forms of the plaintext string and key string into binary form
PlainTextBinary = [format(char, '08b') for char in PlainTextASCII]
#print("PlainTextBinary: ",PlainTextBinary)
KeyBinary = [format(char, '08b') for char in KeyASCII]
#print("KeyBinary: ",KeyBinary)

# Perform XOR between the binary forms of the plaintext string and key string.
# If the length of key string is shorter that the length of plain text string, repeat the the same key string for the rest of the plaintext string.
XORResult = [str(int(a) ^ int(b)) for a, b in zip(PlainTextBinary, KeyBinary)]
#print("XORResult: ", XORResult)

# Proceed to find the ASCII form of the XOR result
XORResultASCII = [chr(int(a)) for a in XORResult]
#print("XORResultASCII: ", XORResultASCII)

# Finally, find the plain text form of the XOR result
PlainTextResult = ''.join(XORResultASCII)
print("PlainTextResult: ", PlainTextResult)
"""

# Take string "Hi class Of 2022" as plaintext and string "CYBER" as key
PlainText = "Hi Class Of 2022"
Key = "CYBER"

# Convert the plaintext string and key string into their ASCII forms
PlainTextASCII = [ord(char) for char in PlainText]
print("PlainTextASCII: ", PlainTextASCII)
KeyASCII = [ord(char) for char in Key]
print("KeyASCII: ", KeyASCII)

# Convert the ASCII forms of the plaintext string and key string into binary form
PlainTextBinary = [format(char, '08b') for char in PlainTextASCII]
print("PlainTextBinary: ", PlainTextBinary)
KeyBinary = [format(char, '08b') for char in KeyASCII]
print("KeyBinary: ", KeyBinary)

# Perform XOR between the binary forms of the plaintext string and key string.
# If the length of key string is shorter than the length of plain text string, repeat the key string for the rest of the plaintext string.
XORResultBinary = []

key_length = len(KeyBinary)
for i in range(len(PlainTextBinary)):
    key_bin = KeyBinary[i % key_length]
    pt_bin = PlainTextBinary[i]
    xor_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(pt_bin, key_bin))
    XORResultBinary.append(xor_bin)
print("XORResultBinary: ", XORResultBinary)

# Convert the XOR result binary to ASCII
XORResultASCII = [int(b, 2) for b in XORResultBinary]
print("XORResultASCII: ", XORResultASCII)

# Finally, find the plain text form of the XOR result
PlainTextResult = ''.join(chr(a) for a in XORResultASCII)
print("PlainTextResult: ", PlainTextResult)
