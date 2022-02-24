import re

participants = input().split(", ")
final = {}
command = input()
while command != "end of race":

    distance = 0
    name = re.findall(r"[a-zA-Z]", command)
    name = "".join(name)
    if name in participants:
        km = re.findall(r"\d", command)
        for k in km:
            distance += int(k)
        if name not in final:
            final[name] = distance
        else:
            final[name] += distance
    command = input()
sorted_p = sorted(final.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {sorted_p[0][0]}")
print(f"2nd place: {sorted_p[1][0]}")
print(f"3rd place: {sorted_p[2][0]}")
