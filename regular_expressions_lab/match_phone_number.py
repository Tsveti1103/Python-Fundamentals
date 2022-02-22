import re

text = input()
matches = re.finditer(r"\+359( |-)2(\1)\d{3}(\1)\d{4}\b", text)
res = ""
for match in matches:
    match_string = match.group(0)
    res += match_string + ", "
print(res.rstrip(", "))
