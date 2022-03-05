price = input()
total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0
while price != "special" and price != "regular":
    price = float(price)
    if price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += price
        total_amount_of_taxes += price * 0.2
        total_price_with_taxes = total_amount_of_taxes + total_price_without_taxes
    price = input()
    if price == "special":
        total_price_with_taxes *= 0.9
if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {total_amount_of_taxes:.2f}$\n"
          f"----------- \n"
          f"Total price: {total_price_with_taxes:.2f}$")
