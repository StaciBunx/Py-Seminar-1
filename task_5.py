# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

point_x_A = int(input("Введите координату Х для А: "))
point_y_A = int(input("Введите координату Y для А: "))
point_x_B = int(input("Введите координату Х для B: "))
point_y_B = int(input("Введите координату Y для B: "))
print(
    f'''Вы ввели: А ({point_x_A},{point_y_A}); B ({point_x_B},{point_y_B})''')

distance = math.sqrt(((point_x_B-point_x_A)**2) + ((point_y_B-point_y_A)**2))
distance = round(distance, 2)
print(
    f'''Расстояние между точками: {distance}''')