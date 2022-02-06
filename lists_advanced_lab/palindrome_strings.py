words = input().split()
palindrome = input()
palindromes = [x for x in words if x == "".join(reversed(x))]

print(palindromes)
count = palindromes.count(palindrome)
print(f"Found palindrome {count} times")
