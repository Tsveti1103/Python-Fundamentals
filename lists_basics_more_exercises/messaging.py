numbers = input().split()
chars = list(input())
current_sum = 0
new_list = []
for number in numbers:
    for i in number:
        current_sum += int(i)
    if len(chars) <= current_sum:
        current_sum -= len(chars)
    new_list.append(chars[current_sum])
    chars.pop(current_sum)
    current_sum = 0
print("".join(new_list))
