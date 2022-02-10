numbers = input().split()
count_of_numbers = int(input())
final_list = []
for index in range(len(numbers)):
    final_list.append(int(numbers[index]))
for i in range(count_of_numbers):
    final_list.remove(min(final_list))
final_list = ", ".join(map(str, final_list))
print(final_list)
