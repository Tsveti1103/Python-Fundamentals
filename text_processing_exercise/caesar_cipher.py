text = input()
new_text = ""
for character in text:
    new_char = ord(character) + 3
    new_text += chr(new_char)
print(new_text)
