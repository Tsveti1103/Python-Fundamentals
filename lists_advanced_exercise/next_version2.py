version = [s for s in input().split(".")]
numbers_string = ""
for digit in version:
    numbers_string += digit
new_version = str(int(numbers_string)+1)
print(".".join(new_version))
