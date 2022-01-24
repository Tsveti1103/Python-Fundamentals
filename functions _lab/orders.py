def calculate_total_price(product, amount):
    product_price = 0
    if product == "coffee":
        product_price = 1.5
    elif product == "water":
        product_price = 1
    elif product == "coke":
        product_price = 1.4
    elif product == "snacks":
        product_price = 2

    total_price = product_price * amount
    return total_price


product = input()
amount = int(input())
res = calculate_total_price(product, amount)
print(f"{res:.2f}")
