input_args = input().split()
table = {}
for i in range(0, len(input_args), 2):
    product = input_args[i]
    quantity = int(input_args[i + 1])
    table[product] = quantity
print(table)
