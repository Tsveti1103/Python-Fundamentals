input_args = input().split()
table = {}

for i in range(0, len(input_args), 2):
    product = input_args[i]
    quantity = int(input_args[i + 1])
    table[product] = quantity

products = input().split()
for p in products:
    if p in table:
        quantity = table[p]
        print(f"We have {quantity} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")
