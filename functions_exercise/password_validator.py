def is_long(string):
    if not 6 <= len(string) <= 10:
        return "Password must be between 6 and 10 characters"

    return True


def letters_and_digits(string):
    if not string.isalnum():
        return "Password must consist only of letters and digits"
    return True


def two_digits(string):
    digits_counter = 0
    for value in string:
        if value.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        return "Password must have at least 2 digits"
    return True


password = input()
first = is_long(password)
second = letters_and_digits(password)
third = two_digits(password)
if first is not True:
    print(first)
if second is not True:
    print(second)
if third is not True:
    print(third)
if first == second == third is True:
    print("Password is valid")
# text = "asdhkh123klkdlas;"
# text.isalnum()  # проверява дали има само букви и цифри
# text.isdigit()  # дали има само цифри
# text.isaplha()  # дали има само букви
# if len_is_ok(passwore) and letters_and_digits(password) and two_digits(password):
#     print("Password is ok")
# result = [a, b, c]
# if all(result) == True:  # ако всички имат еднакъв резултат True
#     print("Password is ok")
