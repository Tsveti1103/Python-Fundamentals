list_os_int = input().split()
opposite_numbers = []
for index in range(len(list_os_int)):
    opposite_number = - int(list_os_int[index])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)