start_index = int(input())
end_index = int(input())
sum_of_char = ""
for i in range(start_index, end_index + 1):
    current_index = chr(i)
    sum_of_char += current_index + " "
print(sum_of_char)
