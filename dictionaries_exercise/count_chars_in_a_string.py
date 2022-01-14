text = input()
characters = {}
for char in text:
    if char != " ":
        if char not in characters:
            characters[char] = 0
        characters[char] += 1

for k, v in characters.items():
    print(f"{k} -> {v}")
