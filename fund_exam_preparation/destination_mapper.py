import re

final = []
travel_points = 0
some_text = input()
some_text = re.finditer(r"(=|\/)(?P<Destination>\b[A-Z][a-zA-Z]+)\1", some_text)
for match in some_text:
    destination = match.group("Destination")
    if len(destination) >= 3:
        travel_points += len(destination)
        final.append(destination)
print(f"Destinations: {', '.join(final)}")
print(f"Travel Points: {travel_points}")
