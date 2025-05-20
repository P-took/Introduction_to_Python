from math import ceil


def square(side):
    return ceil(side * side)


side = float(input('Введите сторону квадрата: '))

print(f'Площадь квадрата - {square(side)}')
