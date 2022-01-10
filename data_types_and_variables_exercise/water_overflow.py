water_tank_capacity = 255
number_of_pours = int(input())
litters_in_tank = 0
for i in range(number_of_pours):
    liters_of_water = int(input())
    litters_in_tank += liters_of_water
    if litters_in_tank > water_tank_capacity:
        print("Insufficient capacity!")
        litters_in_tank -= liters_of_water
        continue
print(litters_in_tank)
