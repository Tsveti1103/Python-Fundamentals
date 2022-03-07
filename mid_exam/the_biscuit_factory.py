import math

number_of_biscuits_per_worker = int(input())
workers_count = int(input())
competition_biscuits = int(input())
total_biscuits = 0
for day in range(1, 31):
    current_biscuits = number_of_biscuits_per_worker * workers_count
    if day % 3 == 0:
        current_biscuits *= 0.75
        current_biscuits = math.floor(current_biscuits)

    total_biscuits += current_biscuits
print(f"You have produced {total_biscuits} biscuits for the past month.")
difference = abs(total_biscuits - competition_biscuits)
percentage = difference / competition_biscuits * 100
if total_biscuits > competition_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
