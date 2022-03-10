number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    car_info = input().split("|")
    car_model = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars[car_model] = {"km": mileage, "fuel": fuel}
command = input().split(" : ")
while command[0] != "Stop":
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        needed_fuel = int(command[3])
        if cars[car]["fuel"] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["km"] += distance
            cars[car]["fuel"] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if cars[car]["km"] >= 100_000:
                del cars[car]
                print(f"Time to sell the {car}!")

    elif command[0] == "Refuel":
        car = command[1]
        refill = int(command[2])
        if (cars[car]["fuel"] + refill) > 75:
            refill = 75 - cars[car]["fuel"]
        cars[car]["fuel"] += refill
        print(f"{car} refueled with {refill} liters")
    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])
        cars[car]["km"] -= kilometers
        if cars[car]["km"] < 10000:
            cars[car]["km"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input().split(" : ")
sorted_cars = sorted(cars.items(), key=lambda kvp: (-kvp[1]["km"], kvp[0]))
for car in sorted_cars:
    print(f"{car[0]} -> Mileage: {car[1]['km']} kms, Fuel in the tank: {car[1]['fuel']} lt.")
