numbers = input().split()
new_numbers = []
for arg in numbers:
    num = float(arg)
    round_num = round(num)
    new_numbers.append(round_num)
print(new_numbers)
