text = input()
power = 0
new_text = ""
for i, c in enumerate(text):
    if c != ">":
        if power == 0:
            new_text += c
        else:
            power -= 1
    else:
        power += int(text[i + 1])
        new_text += ">"
print(new_text)
