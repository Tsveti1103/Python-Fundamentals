import re

total_price = 0
command = input()
furniture_names = []
while command != "Purchase":
    price = 0
    matches = re.findall(r"(?<=>>)([a-zA-Z]+)<<([0-9\.]+)!([0-9]+)", command)
    for match in matches:
        furniture_names.append(match[0])
        price = float(match[1]) * int(match[2])
        total_price += price
    command = input()
print("Bought furniture:")
for furniture in furniture_names:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
