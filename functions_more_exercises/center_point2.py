import math


def point_distance(x_point, y_point):
    return abs(x_point) + abs(y_point)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
first_point_distance = point_distance(x1, y1)
second_point_distance = point_distance(x2, y2)
if first_point_distance <= second_point_distance:
    x = math.floor(x1)
    y = math.floor(y1)
else:
    x = math.floor(x2)
    y = math.floor(y2)
print(f"({x}, {y})")
