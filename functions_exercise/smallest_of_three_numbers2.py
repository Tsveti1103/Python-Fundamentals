import sys


def smallest_number(some_numbers):
    min_number = sys.maxsize
    for number in some_numbers:
        if number < min_number:
            min_number = number
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
print(smallest_number(numbers))
