events = input().split("|")
energy = 100
coins = 100
all_events = True
for event in events:
    event = event.split("-")
    command = event[0]
    number = int(event[1])
    if command == "rest":
        if energy + number > 100:
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins > number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            all_events = False
            break
if all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
