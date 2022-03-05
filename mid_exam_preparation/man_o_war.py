def is_valid(ship, current_index):
    return 0 <= current_index < ship


pirate_ship = [int(p) for p in input().split(">")]
warship = [int(w) for w in input().split(">")]
maximum_health = int(input())
command = input().split()
is_retire = True
while command[0] != "Retire":
    if command[0] == "Fire":
        index = int(command[1])
        warship_damage = int(command[2])
        if is_valid(len(warship), index):
            warship[index] -= warship_damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_retire = False
                break
        command = input().split()
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        pirate_damage = int(command[3])
        if is_valid(len(pirate_ship), start_index) and is_valid(len(pirate_ship), end_index):
            for index in range(start_index, end_index + 1):
                index = int(index)
                pirate_ship[index] -= pirate_damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_retire = False
                    break
        command = input().split()
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if is_valid(len(pirate_ship), index):
            if pirate_ship[index] + health <= maximum_health:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = maximum_health
        command = input().split()
    elif command[0] == "Status":
        counter = 0
        need_repair = 0.2 * maximum_health
        for section in pirate_ship:
            if section < need_repair:
                counter += 1
        print(f"{counter} sections need repair.")
        command = input().split()
if is_retire:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
