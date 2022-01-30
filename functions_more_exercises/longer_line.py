import math


def point_distance(x_point, y_point):
    return x_point + y_point ** 2


def line_length(x_1, y_1, x_2, y_2):
    length = math.sqrt(pow(x_1 - x_2, 2) + pow(y_1 - y_2, 2))
    return length


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
first_point_distance = point_distance(x1, y1)
second_point_distance = point_distance(x2, y2)
third_point_distance = point_distance(x3, y3)
fourth_point_distance = point_distance(x4, y4)
first_line_lenght = line_length(x1, y1, x2, y2)
second_line_lenght = line_length(x3, y3, x4, y4)
if first_line_lenght >= second_line_lenght:
    if first_point_distance <= second_point_distance:
        first_x = math.floor(x1)
        first_y = math.floor(y1)
        second_x = math.floor(x2)
        second_y = math.floor(y2)
    else:
        first_x = math.floor(x2)
        first_y = math.floor(y2)
        second_x = math.floor(x1)
        second_y = math.floor(y1)
else:
    if third_point_distance <= fourth_point_distance:
        first_x = math.floor(x3)
        first_y = math.floor(y3)
        second_x = math.floor(x4)
        second_y = math.floor(y4)
    else:
        first_x = math.floor(x4)
        first_y = math.floor(y4)
        second_x = math.floor(x3)
        second_y = math.floor(y3)
print(f"({first_x}, {first_y})({second_x}, {second_y})")
