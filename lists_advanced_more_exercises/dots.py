rows = int(input())
rows_list = []
first_counter = 0
first_index_list = []
second_counter = 0
second_index_list = 0
for row in range(rows):
    new_row = input().split()
    rows_list.append(new_row)

for index in range(len(rows_list)):
    current_row = rows_list[index]
    if index == 0:
        if not first_index_list:
            for i in range(len(current_row)):
                if "." in current_row[i]:
                    first_index_list.append(i)
                else:
                    second_index_list = first_index_list
                    first_index_list = []
    else:
        if "." in current_row and current_row.index(".") in max(len(first_index_list),len(second_index_list)):
            pass