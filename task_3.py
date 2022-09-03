# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_point = int(input('Введите координату X: '))
y_point = int(input('Введите координату Y: '))
if ((x_point == 0) or (y_point == 0)):
    print("Ошибка!")
elif (x_point > 0 and y_point > 0):
    print(1)
elif (x_point < 0 and y_point > 0):
    print(2)
elif (x_point < 0 and y_point < 0):
    print(3)
elif (x_point > 0 and y_point < 0):
    print(4)


