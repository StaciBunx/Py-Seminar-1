# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = (input('Введите номер четверти (1-4): '))
if (quarter.isdigit() == False):
    print("Введите число!")
elif (quarter != 1 or quarter != 2 or quarter != 3 or quarter != 4):
    print("Ошибка!")
elif (quarter == 1):
    print("Возможные координаты точки в 1 четверти: X > 0, Y > 0")
elif (quarter == 2):
    print("Возможные координаты точки в 2 четверти: X < 0, Y > 0")
elif (quarter == 3):
    print("Возможные координаты точки в 3 четверти: X < 0, Y < 0")
elif (quarter == 4):
    print("Возможные координаты точки в 4 четверти: X > 0, Y < 0")
