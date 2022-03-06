energy = int(input())
command = input()
won_counter = 0
is_end = True
while command != "End of battle":
    distance = int(command)
    if energy - distance >= 0:
        energy -= distance
        won_counter += 1
        if won_counter % 3 == 0:
            energy += won_counter
    else:
        print(f"Not enough energy! Game ends with {won_counter} won battles and {energy} energy")
        is_end = False
        break
    command = input()
if is_end:
    print(f"Won battles: {won_counter}. Energy left: {energy}")
