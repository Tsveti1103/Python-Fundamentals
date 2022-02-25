text = input()
new = ""
for i, c in enumerate(text):
    if i != len(text)-1:
        if c != text[i + 1]:
            new += c
    else:
        new += c
print(new)
