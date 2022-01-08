string = input()
sheeps_list = string.split(", ")
sheeps_list.reverse()
if sheeps_list[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for counter, word in enumerate(sheeps_list):
        counter += 1
        if word == "wolf":
            print(f"Oi! Sheep number {counter-1}! You are about to be eaten by a wolf!")
            break
