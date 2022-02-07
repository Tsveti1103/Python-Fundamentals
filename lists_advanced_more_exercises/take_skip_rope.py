some_string = input()
numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []
result_string_list = []
skipped_string_list = []
is_finish = False
for element in some_string:
    if element.isdigit():
        numbers_list.append(element)
    else:
        non_numbers_list.append(element)

for i, v in enumerate(numbers_list):
    if i % 2 == 0:
        take_list.append(v)
    else:
        skip_list.append(v)
while non_numbers_list:
    if is_finish:
        break
    for index in range(len(take_list)):
        to_take = int(take_list[index])
        if to_take != 0:
            result_string_list += non_numbers_list[:to_take]
            non_numbers_list = non_numbers_list[to_take:]
        to_skip = int(skip_list[index])
        if to_skip != 0:
            skipped_string_list += non_numbers_list[:to_skip]
            non_numbers_list = non_numbers_list[to_skip:]
        if index == len(take_list) - 1:
            is_finish = True

print("".join(result_string_list))
