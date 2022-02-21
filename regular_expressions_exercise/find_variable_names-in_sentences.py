import re

string = input()
matches = re.findall(r"\b_([a-zA-Z0-9]+)\b", string)
print(','.join(matches))
