strings = input().split()
first_string = strings[0]
second_string = strings[1]
total_sum = 0
if len(first_string) == len(second_string):
    for c in range(len(first_string)):
        total_sum += (ord(first_string[c]) * ord(second_string[c]))
else:
    shorter = min(len(first_string), len(second_string))
    longer = max(len(first_string), len(second_string))
    for c in range(shorter):
        total_sum += (ord(first_string[c]) * ord(second_string[c]))
    for c in range(shorter, longer):
        if longer == len(first_string):
            total_sum += ord(first_string[c])
        else:
            total_sum += ord(second_string[c])
print(total_sum)
