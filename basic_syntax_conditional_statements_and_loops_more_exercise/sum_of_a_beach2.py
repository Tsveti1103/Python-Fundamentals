string = input()
string = string.lower()
words = ["sun", "sand", "water", "fish"]
counter = 0
for i in words:
    if i in string:
        counter += string.count(i)
print(counter)
