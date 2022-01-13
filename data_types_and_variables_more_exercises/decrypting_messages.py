key = int(input())
num = int(input())
word = ""
for i in range(num):
    letter = input()
    new_letter = ord(letter) + key
    word += chr(new_letter)
print(word)
