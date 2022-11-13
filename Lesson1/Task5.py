# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве. Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt


def input_coordinates(message):
    names = ['X', 'Y']
    ZERO_POINT = 0.0
    coordinates = [ZERO_POINT, ZERO_POINT]
    for i in range(2):
        print_message = f'{message} {names[i]} - '
        coordinates[i] = float(input(print_message))
    return coordinates


def distance_between_two_points(coordinates_start, coordinates_end):
    distance_x = coordinates_end[0] - coordinates_start[0]
    distance_y = coordinates_end[1] - coordinates_start[1]
    distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2))
    return distance


coordinates_start = input_coordinates(f'Enter coordinate A,')
coordinates_end = input_coordinates(f'Enter coordinate B,')
distance = distance_between_two_points(coordinates_start, coordinates_end)
print(f'-> {distance:.2f}')
