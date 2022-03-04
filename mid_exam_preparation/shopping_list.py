def exists(current_item, shopping_list):
    return current_item in shopping_list


groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    item = command[1]
    if command[0] == "Urgent":
        if not exists(item, groceries):
            groceries.insert(0, item)
    elif command[0] == "Unnecessary":
        if exists(item, groceries):
            groceries.remove(item)
    elif command[0] == "Correct":
        if exists(item, groceries):
            new_item = command[2]
            groceries[groceries.index(item)] = new_item
    elif command[0] == "Rearrange":
        if exists(item, groceries):
            groceries.remove(item)
            groceries.append(item)
    command = input()
print(", ".join(groceries))
