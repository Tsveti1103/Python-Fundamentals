items_price = input().split("|")
budget = float(input())
new_price_list = []
new_price = 0
total_sum = 0
profit = 0
for item in items_price:
    item = item.split("->")
    item_type = item[0]
    item_price = float(item[1])
    if (item_type == "Clothes" and item_price <= 50.00) \
            or (item_type == "Shoes" and item_price <= 35.00) \
            or (item_type == "Accessories" and item_price <= 20.50):
        if budget >= item_price:
            budget -= item_price
            new_price = 1.4 * item_price
            profit += new_price - item_price
            total_sum += new_price
            new_price_list.append(f"{new_price:.2f}")
total_sum += budget
new_price_list = " ".join(new_price_list)
print(new_price_list)
print(f"Profit: {profit:.2f}")
if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
