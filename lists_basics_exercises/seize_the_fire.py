fires = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
list_of_cells = []
for i, v in enumerate(fires):
    new = v.split(" = ")
    if (new[0] == "High" and 81 <= int(new[1]) <= 125) \
            or (new[0] == "Medium" and 51 <= int(new[1]) <= 80) \
            or (new[0] == "Low" and 1 <= int(new[1]) <= 50):
        if amount_of_water < int(new[1]):
            continue
        amount_of_water -= int(new[1])
        total_fire += int(new[1])
        effort += 0.25 * int(new[1])
        list_of_cells.append(new[1])
print("Cells:")
for cell in list_of_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
