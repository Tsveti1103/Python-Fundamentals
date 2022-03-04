def is_valid(current_index, length_targets):
    return len(length_targets) > current_index >= 0 and length_targets[index] != -1


count = 0
targets = [int(e) for e in input().split()]
command = input()
while command != "End":
    index = int(command)
    if is_valid(index, targets):
        value = targets[index]
        targets[index] = -1
        count += 1
        for index, target in enumerate(targets):
            if target != -1:
                if target > value:
                    targets[index] -= value
                else:
                    targets[index] += value
    command = input()
targets = [str(t) for t in targets]
print(f"Shot targets: {count} -> {' '.join(targets)}")
