n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

criteria = input()
filtered = []
is_even = criteria == "even"
is_odd = criteria == "odd"
is_positive = criteria == "positive"
is_negative = criteria == "negative"
for num in numbers:
    if (is_even and num % 2 == 0) \
            or (is_odd and num % 2 != 0) \
            or (is_positive and num >= 0) \
            or (is_negative and num < 0):
        filtered.append(num)
print(filtered)
