text = input().split()
total_sum = 0
for character in text:
    first_letter = character[0]
    number = int(character[1:-1])
    second_letter = character[-1]
    if first_letter.isupper():
        position = ord(first_letter) - 64
        number = number / position
    else:
        position = ord(first_letter) - 96
        number = number * position

    if second_letter.isupper():
        position = ord(second_letter) - 64
        number = number - position
    else:
        position = ord(second_letter) - 96
        number = number + position
    total_sum += number
print(f"{total_sum:.2f}")
