food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
pig_weight = float(input())
is_enough = True
for day in range(1, 31):
    food_quantity = float(f"{food_quantity - 0.3:.2f}")
    if day % 2 == 0:
        hay_quantity -= float(f"{0.05 * food_quantity:.2f}")
    if day % 3 == 0:
        cover_quantity -= float(f"{pig_weight / 3}")
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        print("Merry must go to the pet store!")
        is_enough = False
        break
if is_enough:
    print(
        f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
