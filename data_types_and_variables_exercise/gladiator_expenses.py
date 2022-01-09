lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_brakes = 0
for lost in range(1, lost_fights_count + 1):
    if lost % 2 == 0:
        expenses += helmet_price
    if lost % 3 == 0:
        expenses += sword_price
        if lost % 2 == 0:
            expenses += shield_price
            shield_brakes += 1
    if shield_brakes == 2:
        expenses += armor_price
        shield_brakes = 0
print(f"Gladiator expenses: {expenses:.2f} aureus")
