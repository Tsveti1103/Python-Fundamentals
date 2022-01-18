command = input().split()
order = {}
while command[0] != "buy":
    product = command[0]
    current_price = float(command[1])
    current_quantity = int(command[2])
    if product not in order:
        order[product] = [current_quantity, current_price]
    else:
        order[product][0] += current_quantity
        order[product][1] = current_price
        # one = order[product][0]
        # two = order[product][1]
        # print(one * two)
    command = input().split()
for product, price in order.items():
    total_price = price[0] * price[1]
    print(f"{product} -> {total_price:.2f}")
