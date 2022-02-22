import re

numbers = input()
matches = re.finditer(r"(\d{2})([-.\/])([A-Z][a-z]{2})(\2)(\d{4})", numbers)
for match in matches:
    day = match.group(1)
    mouth = match.group(3)
    year = match.group(5)
    print(f"Day: {day}, Month: {mouth}, Year: {year}")
