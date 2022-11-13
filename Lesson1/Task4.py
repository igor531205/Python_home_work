# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def coordinate_range(quarter):
    FIRST_QUARTER = 1
    SECOND_QUARTER = 2
    THIRD_QUARTER = 3
    FOURTH_QUARTER = 4
    if quarter == FIRST_QUARTER:
        return f'X = (0, +∞); Y = (0, +∞]'
    elif quarter == SECOND_QUARTER:
        return f'X = [-∞, 0); Y = (0, +∞]'
    elif quarter == THIRD_QUARTER:
        return f'X = [-∞, 0); Y = [-∞, 0)'
    elif quarter == FOURTH_QUARTER:
        return f'X = (0, +∞]; Y = [-∞, 0)'


quarter = int(input(f'Enter quarter of the coordinates '))
print(coordinate_range(quarter))
