command = input()
counter = 0
while command != "END":
    if command == "cat" or command == "dog" or command == "movie" or command == "coding":
        counter += 1
    elif command == "CAT" or command == "DOG" or command == "MOVIE" or command == "CODING":
        counter += 2
    command = input()
if counter <= 5:
    print(counter)
elif counter > 5:
    print('You need extra sleep')
