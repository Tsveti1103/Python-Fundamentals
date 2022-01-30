def tribonacci(lenght):
    for i in range(length_of_list - 1):
        if len(new_list) < 3:
            current_number = sum(new_list)
            new_list.append(current_number)
        else:
            current_number = new_list[i] + new_list[i - 1] + new_list[i - 2]
            new_list.append(current_number)
    return new_list


length_of_list = int(input())
new_list = [1]
print(*tribonacci(length_of_list))
