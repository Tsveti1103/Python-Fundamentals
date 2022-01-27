def get_symbols(first, second):
    return [chr(s) for s in range(ord(first) + 1, ord(second))]


first_string = input()
second_string = input()
result = get_symbols(first_string, second_string)
print(*result)
