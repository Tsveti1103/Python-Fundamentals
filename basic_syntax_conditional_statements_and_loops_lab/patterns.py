rows = int(input())
for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print("*", end="")
    print()

for row in range(rows - 1, 0, -1):
    for col in range(1, row + 1):
        print("*", end="")
    print()
