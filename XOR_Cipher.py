# Take string "Hi class Of 2022" as plaintext and string "CYBER" as key
PlainText = "Hi Class Of 2022"
Key = "CYBER"

# Convert the plaintext string and key string into their ASCII forms
PlainTextASCII = [ord(char) for char in PlainText]
print("PlainTextASCII: ", PlainTextASCII)
# Convert the ASCII forms of the plaintext string and key string into binary form
# Perform XOR between the binary forms of the plaintext string and key string.
# If the length of key string is shorter that the length of plain text string, repeat the the same key string for the rest of the plaintext string.
# Proceed to find the ASCII form of the XOR result
# Finally, find the plain text form of the XOR result
# Display the plain text form of the XOR Result