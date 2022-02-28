first_symbol = ord(input())
second_symbol = ord(input())
string = input()
sum = 0
for i in range(first_symbol + 1, second_symbol):
    for c in string:
        if ord(c) == i:
            sum += ord(c)
print(sum)
