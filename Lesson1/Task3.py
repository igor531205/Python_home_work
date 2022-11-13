# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится). Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

def input_coordinates(message):
    names = ['X', 'Y']
    ZERO_POINT = 0.0
    coordinates = [ZERO_POINT, ZERO_POINT]
    for i in range(2):
        while coordinates[i] == ZERO_POINT:
            print_message = f'{message} {names[i]} - '
            coordinates[i] = float(input(print_message))
    return coordinates


def quarter_of_the_coordinates(coordinates):
    ZERO_POINT = 0.0
    FIRST_QUARTER = 1
    SECOND_QUARTER = 2
    THIRD_QUARTER = 3
    FOURTH_QUARTER = 4
    if coordinates[0] > ZERO_POINT and coordinates[1] > ZERO_POINT:
        return FIRST_QUARTER
    elif coordinates[0] < ZERO_POINT and coordinates[1] > ZERO_POINT:
        return SECOND_QUARTER
    elif coordinates[0] < ZERO_POINT and coordinates[1] < ZERO_POINT:
        return THIRD_QUARTER
    elif coordinates[0] > ZERO_POINT and coordinates[1] < ZERO_POINT:
        return FOURTH_QUARTER


coordinates = input_coordinates(f'Enter coordinate')
quarter = quarter_of_the_coordinates(coordinates)
print(f'Quarter of the coordinates {quarter}')
