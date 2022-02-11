n = int(input())
word = input()
strings = []
filtered = []
for i in range(n):
    string = input()
    strings.append(string)
    if word in string:
        filtered.append(string)

print(strings)
print(filtered)