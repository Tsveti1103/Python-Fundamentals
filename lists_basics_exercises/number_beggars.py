sums_list = input().split(", ")
number_of_beggars = int(input())
final_list = []
counter_of_index = 0
temp_sum = 0
sums_list_as_digits = []
for index in range(len(sums_list)):
    sums_list_as_digits.append(int(sums_list[index]))
while counter_of_index < number_of_beggars:
    for element in range(counter_of_index, len(sums_list_as_digits), number_of_beggars):
        temp_sum += sums_list_as_digits[element]
    final_list.append(temp_sum)
    temp_sum = 0
    counter_of_index += 1
print(final_list)