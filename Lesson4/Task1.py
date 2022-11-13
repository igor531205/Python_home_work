# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi


def user_input_number(message, begin, end):
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :param begin: Начальное значение ввода.
    :param end: Конечное значение ввода.
    :return: Натуральное число, введеное пользователем.
    """
    number = int()
    while not (begin <= number <= end):
        string = input(f'{message}')
        number = int(string) if string.isdigit() else int()
    return number


def round_number(number, precision):
    """Округление числа с заданной точностью.
    :param number: Число для округления.
    :param precision: Необходимая точность.
    :return: Число полученное после округления.
    """
    return int(number / precision) * precision


PRECISION_MIN = 1
PRECISION_MAX = 10
MESSAGE_FOR_USER = \
    f'Please enter the number of digits to round: for {PRECISION_MIN} to {PRECISION_MAX} -> '
precision_d = \
    float(10 ** -(user_input_number(MESSAGE_FOR_USER, PRECISION_MIN, PRECISION_MAX)))
number = round_number(pi, precision_d)
print(f'Precision d = {precision_d}, π = {number}')
