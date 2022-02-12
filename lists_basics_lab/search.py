n = int(input())
word = input()
strings = []
for i in range(n):
    strings.append(input())
filtered = []
for string in strings:
    if word in string:
        filtered.append(string)

print(strings)
print(filtered)