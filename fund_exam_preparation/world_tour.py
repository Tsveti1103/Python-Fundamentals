def is_valid(index, string):
    return 0 <= index < len(string)


stops = input()
command_input = input().split(":")
while command_input[0] != "Travel":
    command = command_input[0]
    if command == "Add Stop":
        index = int(command_input[1])
        string = command_input[2]
        if is_valid(index, stops):
            stops = stops[:index] + string + stops[index:]
        print(f"{stops}")
    elif command == "Remove Stop":
        start_index = int(command_input[1])
        end_index = int(command_input[2])
        if is_valid(start_index, stops) and is_valid(end_index, stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(f"{stops}")
    elif command == "Switch":
        old_string = command_input[1]
        new_string = command_input[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(f"{stops}")
    command_input = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")
