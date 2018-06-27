"""
Package Creating
"""
from pack.sub.first import sq, circle

print("площадь квадрата")
x = input("Сторона равна: ")
print(">>>Площадь равна:{}".format(sq(x)))
circle_rad = input("Радиус круга: ")
print(">>>Площадь круга:{}".format(circle(circle_rad)))