def is_valid(current_index, targets_list):
    return 0 <= current_index < len(targets_list)


targets = [int(t) for t in input().split()]
command = input().split()
while command[0] != "End":
    index = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if is_valid(index, targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command[0] == "Add":
        if is_valid(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if is_valid(index + value, targets) and is_valid(index - value, targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")
    command = input().split()
targets = [str(e) for e in targets]
print("|".join(targets))
