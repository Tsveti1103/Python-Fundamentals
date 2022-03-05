def is_valid_index(index, list_length):
    return 0 <= index < list_length


items = input().split()

command_input = input()
moves_counter = 0

while command_input != "end":
    command_args = command_input.split()
    index_one = int(command_args[0])
    index_two = int(command_args[1])
    moves_counter += 1

    if index_one == index_two or not is_valid_index(index_one, len(items)) or not is_valid_index(index_two,
                                                                                                 len(items)):
        new_item = f"-{moves_counter}a"
        middle_index = len(items) // 2
        items.insert(middle_index, new_item)
        items.insert(middle_index, new_item)
        print("Invalid input! Adding additional elements to the board")
        command_input = input()
        continue
    if items[index_one] != items[index_two]:
        print("Try again!")
        command_input = input()
        continue

    removed_item = items.pop(index_one)
    items.remove(removed_item)
    print(f"Congrats! You have found matching elements - {removed_item}!")
    command_input = input()
    if not items:
        break
if items:
    print("Sorry you lose :(")
    print(" ".join(items))
else:
    print(f"You have won in {moves_counter} turns!")
