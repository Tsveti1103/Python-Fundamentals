def exists(current_item, invetory):
    return current_item in invetory


inventory = input().split(", ")
command = input().split(" - ")
while command[0] != "Craft!":
    item = command[1]
    if command[0] == "Collect":
        if not exists(item, inventory):
            inventory.append(item)
    elif command[0] == "Drop":
        if exists(item, inventory):
            inventory.remove(item)
    elif command[0] == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if exists(old_item, inventory):
            item_index = inventory.index(old_item)
            inventory.insert(item_index+1, new_item)
    elif command[0] == "Renew":
        if exists(item, inventory):
            index = inventory.index(item)
            renew_item = inventory.pop(index)
            inventory.append(renew_item)

    command = input().split(" - ")
print(", ".join(inventory))