numbers = input().split()
new_numbers = []
for arg in numbers:
    num = float(arg)
    abs_num = abs(num)
    new_numbers.append(abs_num)
print(new_numbers)
