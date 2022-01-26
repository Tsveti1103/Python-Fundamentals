def is_perfect(some_number):
    sum_of_numbers = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum_of_numbers += divisor
    if sum_of_numbers == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))

