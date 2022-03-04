chest = input().split("|")
command_input = input()
while command_input != "Yohoho!":
    command_args = command_input.split()
    command = command_args[0]
    if command == "Loot":
        items = command_args[1:]
        for element in items:
            if element not in chest:
                chest.insert(0, element)

    elif command == "Drop":
        index = int(command_args[1])
        if index < 0 or index >= len(chest):
            command_input = input()
            continue
        removed_item = chest.pop(index)
        chest.append(removed_item)
    elif command == "Steal":
        count = int(command_args[1])
        steal_item = chest[-count:]
        chest = chest[:-count]
        print(", ".join(steal_item))
    command_input = input()
sum = 0
chest_length = len(chest)
if chest:
    for element in chest:
        sum += len(element)
    average = sum / chest_length
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")