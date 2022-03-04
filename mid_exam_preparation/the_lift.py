people = int(input())
lift = input().split()
for cabin in lift:
    current_cabin = int(cabin)
    free_spaces = 4 - current_cabin
    if people - free_spaces >= 0:
        people -= free_spaces
        lift[lift.index(cabin)] = "4"
    else:
        occupied_spaces = 4 - free_spaces
        current_cabin = occupied_spaces + people
        lift[lift.index(cabin)] = str(current_cabin)
        people = 0
        break
full_wagons = lift.count("4")
if people == 0:
    if full_wagons < len(lift):
        print(f"The lift has empty spots!")
        print(" ".join(lift))
    elif full_wagons == len(lift):
        print(" ".join(lift))
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(lift))
