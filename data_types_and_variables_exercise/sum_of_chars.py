number_of_characters = int(input())
ascii_sum = 0
for characters in range(number_of_characters):
    new_character = input()
    ascii_sum += ord(new_character)
print(f"The sum equals: {ascii_sum}")
