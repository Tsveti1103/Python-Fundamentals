def sorting_numbers(list_of_numbers):
    return sorted(list_of_numbers)


numbers = input().split()
numbers_as_digits = []
for number in numbers:
    numbers_as_digits.append(int(number))
sorted_numbers = sorting_numbers(numbers_as_digits)
print(sorted_numbers)
