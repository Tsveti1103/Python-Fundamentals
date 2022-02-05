words = input().split()
print('\n'.join(s for s in words if len(s) % 2 == 0))
