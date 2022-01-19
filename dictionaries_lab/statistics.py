command = input()
products = {}
while command != "statistics":
    input_args = command.split(": ")
    p = input_args[0]
    q = int(input_args[1])
    if p not in products:
        products[p] = 0
    products[p] += q
    command = input()

print("Products in stock:")
for k, v in products.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(products)}")
sum = sum(products.values())
print(f"Total Quantity: {sum}")
