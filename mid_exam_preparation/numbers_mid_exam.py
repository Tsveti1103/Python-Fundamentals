numbers = [int(n) for n in input().split()]
average = sum(numbers) / len(numbers)
top_numbers = []
while numbers:
    num = max(numbers)
    if num > average:
        top_numbers.append(num)
        numbers.remove(num)
        if len(top_numbers) == 5:
            break
    else:
        numbers.remove(num)
if top_numbers:
    top_numbers = sorted(top_numbers, reverse=True)
    print(*top_numbers)
else:
    print("No")
