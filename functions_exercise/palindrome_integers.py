def palindrome(list_of_numbers):
    for number in list_of_numbers:
        reverse_number = number[::-1]
        if number == reverse_number:
            print(True)
        else:
            print(False)


numbers = input().split(", ")
palindrome(numbers)
