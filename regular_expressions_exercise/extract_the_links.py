import re

text = input()
while True:
    if text:
        matches = re.findall(r"\bwww\.[a-zA-Z-0-9]+\.[a-z\.a-z]+\b", text)
        if matches:
            print(''.join(matches))
    else:
        break
    text = input()
