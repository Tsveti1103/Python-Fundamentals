text = input()
for i, c in enumerate(text):
    if c == ":":
        print(f":{text[i + 1]}")
