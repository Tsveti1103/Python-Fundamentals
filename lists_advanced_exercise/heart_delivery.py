def give_hearts(houses, house_index):
    houses[house_index] -= 2
    if houses[house_index] <= -2:
        print(f"Place {house_index} already had Valentine's day.")
    elif houses[house_index] <= 0:
        print(f"Place {house_index} has Valentine's day.")
    return houses


neighbors = [int(number) for number in input().split("@")]
cuppidon_position = 0
command = input().split()
while command[0] != "Love!":
    value = int(command[1])
    cuppidon_position += value
    if cuppidon_position >= len(neighbors):
        cuppidon_position = 0
    neighbors = give_hearts(neighbors, cuppidon_position)
    command = input().split()
print(f"Cupid's last position was {cuppidon_position}.")
failed_houses = [int(house) for house in neighbors if int(house) > 0]
if failed_houses:
    print(f"Cupid has failed {len(failed_houses)} places.")
else:
    print("Mission was successful.")
