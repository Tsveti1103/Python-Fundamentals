import re

numbers = input()
matches = re.finditer(r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))", numbers)
for match in matches:
    print(match.group(0), end=" ")
