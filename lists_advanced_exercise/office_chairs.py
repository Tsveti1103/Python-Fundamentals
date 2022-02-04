numbers_of_rooms = int(input())
room = 1
total_free_chairs = 0
is_ok = True
while room <= numbers_of_rooms:
    chairs_and_visitors = input().split()
    chairs = chairs_and_visitors[0]
    visitors = int(chairs_and_visitors[1])
    if len(chairs) < visitors:
        needed_chairs_in_room = visitors - len(chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
        is_ok = False
    else:
        free_chairs = len(chairs) - visitors
        total_free_chairs += free_chairs
    room += 1
if is_ok:
    print(f"Game On, {total_free_chairs} free chairs left")
