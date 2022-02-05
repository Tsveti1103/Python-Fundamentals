message = input().split()
secret_massage = []
for word in message:
    number = ""
    character = ""
    for char in word:
        if char.isdigit():
            number += char
    character = chr(int(number))
    word = word.replace(number, character)
    if len(word) > 2:
        word = list(word)
        word[1], word[-1] = word[-1], word[1]
    secret_massage.append("".join(word))
print(*secret_massage)
