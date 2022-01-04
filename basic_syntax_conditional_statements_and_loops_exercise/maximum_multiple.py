divisor = int(input())
boundary = int(input())
final_number = 0
for current_number in range(1, boundary + 1):
    if current_number % divisor == 0:
        final_number = current_number

print(final_number)
