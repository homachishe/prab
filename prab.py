import math

x1, y1 = map(float, input('Enter the coordinates of point A separated by a space: ').split())
x2, y2 = map(float, input('Enter the coordinates of point B separated by a space: ').split())
length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
midpoint_x = (x1 + x2) / 2
midpoint_y = (y1 + y2) / 2
print('Length of the segment AB:', length)
print('Coordinates of the middle of the segment AB:', midpoint_x, midpoint_y)