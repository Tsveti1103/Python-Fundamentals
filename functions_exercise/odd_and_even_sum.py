def get_even_and_odd_numbers(number):
    even_numbers_sum = 0
    odd_numbers_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_numbers_sum += int(digit)
        else:
            odd_numbers_sum += int(digit)
    return even_numbers_sum, odd_numbers_sum


number_as_string = input()
even_sum, odd_sum = get_even_and_odd_numbers(number_as_string)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
