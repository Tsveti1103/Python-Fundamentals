def multiplication(a, b, c):
    negative_counter = 0
    result = "positive"
    if a < 0:
        negative_counter += 1
    if b < 0:
        negative_counter += 1
    if c < 0:
        negative_counter += 1
    if negative_counter % 2 != 0:
        result = "negative"
    if a == 0 or b == 0 or c == 0:
        result = "zero"
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication(first_number, second_number, third_number))
