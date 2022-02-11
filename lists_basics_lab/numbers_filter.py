n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

criteria = input()
filtered = []
for num in numbers:
    if criteria == "even" and num % 2 == 0:
        filtered.append(num)
    elif criteria == "odd" and num % 2 != 0:
        filtered.append(num)
    elif criteria == "positive" and num >= 0:
        filtered.append(num)
    elif criteria == "negative" and num < 0:
        filtered.append(num)
print(filtered)