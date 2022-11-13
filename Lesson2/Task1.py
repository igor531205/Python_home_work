# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр. Пример:
# - 6782 -> 23
# - 0,56 -> 11


def user_input(message):
    '''пользовательский ввод'''
    string = None
    while not string:
        string = input(f'{message}')
    return string


def sum_of_digits_in_number(number):
    '''расчет суммы цифр в числе'''
    ZERRO_DIGIT = 0
    sum_of_digits = ZERRO_DIGIT
    for digit in number:
        sum_of_digits += int(digit) if digit.isdigit() else ZERRO_DIGIT
    return sum_of_digits


MESSAGE_FOR_USER = 'Please enter a real number -> '
string = user_input(f'{MESSAGE_FOR_USER}')
sum_of_digits = sum_of_digits_in_number(string)
print(f'{sum_of_digits}')
