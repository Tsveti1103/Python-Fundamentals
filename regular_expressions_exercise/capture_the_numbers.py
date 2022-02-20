import re

result = []
text = input()
while True:
    if text:
        matches = re.findall(r"\d+", text)
        if matches:
            print(" ".join(matches), end=" ")
        text = input()
    else:
        break
