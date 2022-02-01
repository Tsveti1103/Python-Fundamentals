def collect(inventory, current_item):
    if current_item not in inventory:
        inventory.append(current_item)
    return inventory


def drop(inventory, current_item):
    if current_item in inventory:
        inventory.remove(current_item)
    return inventory


def combine_items(inventory, item_old, item_new):
    if item_old in inventory:
        inventory.insert(inventory.index(item_old) + 1, item_new)
    return inventory


def renew(inventory, current_item):
    if current_item in inventory:
        inventory.append(inventory.pop(inventory.index(current_item)))
    return inventory


items_in_inventory = input().split(", ")
command = input().split(" - ")
while command[0] != "Craft!":
    action = command[0]
    item = command[1]
    if action == "Collect":
        items_in_inventory = collect(items_in_inventory, item)
    elif action == "Drop":
        items_in_inventory = drop(items_in_inventory, item)
    elif action == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        items_in_inventory = combine_items(items_in_inventory, old_item, new_item)
    elif action == "Renew":
        items_in_inventory = renew(items_in_inventory, item)
    command = input().split(" - ")
print(", ".join(items_in_inventory))
