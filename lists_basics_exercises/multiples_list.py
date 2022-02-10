factor = int(input())
count = int(input())
my_list = [factor]
for number in range(factor + 1, count * factor + 1):
    if (number + factor) % factor == 0:
        my_list.append(number)
print(my_list)
