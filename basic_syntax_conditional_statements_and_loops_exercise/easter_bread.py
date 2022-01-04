budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
bread_price = flour_price + eggs_price + milk_price
colored_eggs = 0
number_of_bread = 0
while budget >= bread_price:
    number_of_bread += 1
    budget -= bread_price
    colored_eggs += 3
    if number_of_bread % 3 == 0:
        colored_eggs -= number_of_bread - 2
print(f"You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
