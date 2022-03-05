houses = [int(e) for e in input().split("@")]
command = input()
cupid_position = 0
counter = 0
valentine_houses = []
while command != "Love!":
    command = command.split()
    jump = int(command[1])
    if jump + cupid_position >= len(houses):
        cupid_position = 0
        if houses[cupid_position] == 0:
            print(f"Place {cupid_position} already had Valentine's day.")
        else:
            houses[cupid_position] -= 2
            if houses[cupid_position] == 0:
                print(f"Place {cupid_position} has Valentine's day.")
                counter += 1
    else:
        cupid_position += jump
        if houses[cupid_position] == 0:
            print(f"Place {cupid_position} already had Valentine's day.")
        else:
            houses[cupid_position] -= 2
            if houses[cupid_position] == 0:
                print(f"Place {cupid_position} has Valentine's day.")
                counter += 1
    command = input()
print(f"Cupid's last position was {cupid_position}.")
valentine_houses = [e for e in houses if e == 0]
if len(valentine_houses) == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - len(valentine_houses)} places.")
