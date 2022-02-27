ban_list = input().split(", ")
text = input()
for word in ban_list:
    while word in text:
        rep = "*" * len(word)
        text = text.replace(word, rep)
print(text)
