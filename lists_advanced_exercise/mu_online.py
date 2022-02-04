health = 100
bitcoins = 0
dungeon = input().split("|")
beat_the_dungeon = True
for index, room in enumerate(dungeon):
    room = room.split()
    command = room[0]
    number = int(room[1])
    if command == "potion":
        health += number
        if health > 100:
            number = number - (health - 100)
            health = 100
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index + 1}")
            beat_the_dungeon = False
            break
if beat_the_dungeon:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
