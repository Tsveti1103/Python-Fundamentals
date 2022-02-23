import re

final_price = 0
command = input()
while command != "end of shift":
    name = re.findall(r"(?<=%)(\b[A-Z][a-z]+)%", command)
    product = re.findall(r"(?<=<)(\w+)>", command)
    count = re.findall(r"\|(\d+)\|", command)
    price = re.findall(r"([0-9]+[\.0-9]+)\$", command)
    if name and product and count and price:
        total_price = int(count[0]) * float(price[0])
        print(f"{name[0]}: {product[0]} - {total_price:.2f}")
        final_price += total_price
    command = input()
print(f"Total income: {final_price:.2f}")
