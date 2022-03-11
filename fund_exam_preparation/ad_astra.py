import re

days = 0
text = input()
product_info = re.findall(r"(#|\|)([a-zA-Z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)", text)
for item in product_info:
    calories = int(item[5])
    days += calories
days = int(days / 2000)
print(f"You have food to last you for: {days} days!")
for product in product_info:
    name = product[1]
    date = product[3]
    calories = int(product[5])
    print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")
