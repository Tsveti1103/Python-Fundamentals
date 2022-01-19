words = input().split()
dictionary = {}
for word in words:
    lower_word = word.lower()
    if lower_word not in dictionary:
        dictionary[lower_word] = 0
    dictionary[lower_word] += 1
for key, v in dictionary.items():
    if v % 2 != 0:
        print(key, end=" ")
