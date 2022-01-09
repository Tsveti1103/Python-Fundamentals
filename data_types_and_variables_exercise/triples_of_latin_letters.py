number_of_characters = int(input())
for first in range(number_of_characters):
    for second in range(number_of_characters):
        for third in range(number_of_characters):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}")
