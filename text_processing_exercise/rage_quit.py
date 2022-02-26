def unique(string):
    counter = 0
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
            counter += 1
    return counter


text = input().upper()
new_text = ""
current_text = ""
for index in range(len(text)):
    char = text[index]
    if char.isdigit():
        if index < len(text) - 1:
            if text[index + 1].isdigit():
                number = int(char + text[index + 1])
            else:
                number = int(char)
            new_text += current_text * number
            current_text = ""
        else:
            number = int(char)
            new_text += current_text * number
            current_text = ""
    else:
        current_text += char

if new_text:
    counter = unique(new_text)
    print(f"Unique symbols used: {counter}")
    print(new_text)
else:
    counter = unique(current_text)
    print(f"Unique symbols used: {counter}")
    print(current_text)
