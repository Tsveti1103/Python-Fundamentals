rows = int(input())
rows_list = []
counter = 0
for row in range(rows):
    current_row = input().split()
    rows_list.append(current_row)

attacked_squares = input().split()
for square in attacked_squares:
    attacked_row = int(square[0])
    attacked_col = int(square[2])
    attack = rows_list[attacked_row]
    if int(attack[attacked_col]) > 0:
        attack[attacked_col] = int(attack[attacked_col]) - 1
        if attack[attacked_col] == 0:
            counter += 1

print(counter)
