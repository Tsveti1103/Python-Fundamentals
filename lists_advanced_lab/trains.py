wagon_count = int(input())
wagons = [0] * wagon_count  # wagons = [0 for x in range(wagon_count)]
command_input = input()
while command_input != "End":
    command_args = command_input.split(" ")
    command = command_args[0]
    first_num = int(command_args[1])

    if command == "add":
        wagons[-1] += first_num
    elif command == "insert":
        second_num = int(command_args[2])
        wagons[first_num] += second_num
    elif command == "leave":
        second_num = int(command_args[2])
        wagons[first_num] -= second_num
    command_input = input()
print(wagons)
