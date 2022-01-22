command = input().split(":")
contests = {}
students = {}
while command[0] != "end of contests":
    contest = command[0]
    password = command[1]
    contests[contest] = password
    command = input().split(":")
submission = input().split("=>")
while submission[0] != "end of submissions":
    sub_contest = submission[0]
    sub_password = submission[1]
    username = submission[2]
    points = int(submission[3])
    if sub_contest in contests:
        if sub_password == contests[sub_contest]:
            if username not in students:
                students[username] = {sub_contest: points}
            else:
                if sub_contest not in students[username]:
                    students[username][sub_contest] = points
                else:
                    if points > students[username][sub_contest]:
                        students[username][sub_contest] = points
    submission = input().split("=>")
best = {}
for k, v in students.items():
    best[k] = 0
    for key, value in v.items():
        best[k] += value
max_points = max(best.values())
for candidate, points in best.items():
    if points == max_points:
        winner = candidate
print(f"Best candidate is {winner} with total {max_points} points.")
print('Ranking:')
for k, v in sorted(students.items(), key=lambda x: x[0]):
    print(f'{k}')
    for kk, vv in sorted(v.items(), key=lambda x: -x[1]):
        print(f'#  {kk} -> {vv}')
