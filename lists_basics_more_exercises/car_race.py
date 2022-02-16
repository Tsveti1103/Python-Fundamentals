track = input().split()
middle_of_track = len(track) // 2
left_racer = track[0:middle_of_track]
right_racer = track[-1:middle_of_track:-1]
left_racer_time = 0
right_racer_time = 0
for left in left_racer:
    time = int(left)
    left_racer_time += time
    if time == 0:
        left_racer_time *= 0.8
for right in right_racer:
    time = int(right)
    right_racer_time += time
    if time == 0:
        right_racer_time *= 0.8
if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
elif left_racer_time > right_racer_time:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
