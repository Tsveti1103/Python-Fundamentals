def numbers_max(numbers_list):
    max_number = max(numbers_list)
    return int(max_number)


def numbers_min(numbers_list):
    min_number = min(numbers_list)
    return int(min_number)


def numbers_sum(numbers_list):
    sum_of_numbers = sum(numbers_as_digits)
    return sum_of_numbers


numbers = input().split()
numbers_as_digits = []
for number in numbers:
    numbers_as_digits.append(int(number))
print(f"The minimum number is {numbers_min(numbers_as_digits)}")
print(f"The maximum number is {numbers_max(numbers_as_digits)}")
print(f"The sum number is: {numbers_sum(numbers_as_digits)}")
