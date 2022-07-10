'''3. Напишите программу, которая принимает на вход координаты точки (X и Y),причём X ≠ 0 и Y ≠ 0
 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

*Пример:*

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

coordinate_number_x = int(input("Введите координату X:  "))
coordinate_number_y = int(input("Введите координату Y:  "))

def CoordinateSystem (x, y):
    if x > 0 and y > 0:
        print("Диапазон координат 1 четверти")
    elif x < 0 and y > 0:
        print("Диапазон координат 2 четверти")
    elif x < 0 and y < 0:
        print("Диапазон координат 3 четверти")
    elif x > 0 and y < 0:
        print("Диапазон координат 4 четверти")
    return x, y

CoordinateSystem (coordinate_number_x, coordinate_number_y)