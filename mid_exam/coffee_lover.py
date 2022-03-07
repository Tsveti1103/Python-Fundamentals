def is_valide(current_index, inventory):
    return 0 <= current_index < len(inventory)


coffees_in_stock = input().split()
commands_count = int(input())
for i in range(commands_count):
    command = input().split()
    if command[0] == "Include":
        coffees_in_stock.append(command[1])
    elif command[0] == "Remove":
        count = int(command[2])
        if is_valide(count, coffees_in_stock):
            if command[1] == "first":
                coffees_in_stock = coffees_in_stock[count:]
            elif command[1] == "last":
                num = len(coffees_in_stock) - count
                coffees_in_stock = coffees_in_stock[:num]
    elif command[0] == "Prefer":
        index_one = int(command[1])
        index_two = int(command[2])
        if is_valide(index_one, coffees_in_stock) and is_valide(index_two, coffees_in_stock):
            coffees_in_stock[index_one], coffees_in_stock[index_two] = coffees_in_stock[index_two], coffees_in_stock[
                index_one]
    elif command[0] == "Reverse":
        coffees_in_stock.reverse()
print(f"Coffees:\n{' '.join(coffees_in_stock)}")
