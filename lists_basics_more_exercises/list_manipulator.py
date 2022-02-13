start_list = input().split()
start_list = list(map(int, start_list))
command = input().split()
is_change = True
even_list = []
odd_list = []
while command[0] != "end":
    if is_change:
        even_list = []
        odd_list = []
        for index in range(len(start_list)):
            current_number = start_list[index]
            if current_number % 2 == 0:
                even_list.append(current_number)
            elif current_number % 2 != 0:
                odd_list.append(current_number)
    is_change = False
    if command[0] == "max":
        if command[1] == "odd":
            if odd_list:
                max_odd = len(start_list) - start_list[::-1].index(max(odd_list)) - 1
                print(max_odd)
            else:
                print("No matches")
        elif command[1] == "even":
            if even_list:
                max_even = len(start_list) - start_list[::-1].index(max(even_list)) - 1
                print(max_even)
            else:
                print("No matches")
    elif command[0] == "min":
        if command[1] == "odd":
            if odd_list:
                min_odd = len(start_list) - start_list[::-1].index(min(odd_list)) - 1
                print(min_odd)
            else:
                print("No matches")
        elif command[1] == "even":
            if even_list:
                min_even = len(start_list) - start_list[::-1].index(min(even_list)) - 1
                print(min_even)
            else:
                print("No matches")
    elif command[0] == "first":
        count = int(command[1])
        if count > len(start_list):
            print("Invalid count")
        else:
            if command[2] == "odd":
                print(odd_list[:count])
            elif command[2] == "even":
                print(even_list[:count])
    elif command[0] == "last":
        count = int(command[1])
        if count > len(start_list):
            print("Invalid count")
        else:
            if command[2] == "odd":
                if count <= len(odd_list):
                    num = len(odd_list) - count
                    print(odd_list[num:])
                else:
                    print(odd_list)
            elif command[2] == "even":
                if count <= len(even_list):
                    num = len(even_list) - count
                    print(even_list[num:])
                else:
                    print(even_list)
    elif command[0] == "exchange":
        exchange_index = int(command[1])
        if exchange_index > len(start_list) - 1 or exchange_index < 0:
            print("Invalid index")
        else:
            start_list = start_list[exchange_index + 1:] + start_list[:exchange_index + 1]
            is_change = True
    command = input().split()

print(start_list)
