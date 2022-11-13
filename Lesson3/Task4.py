# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def user_input_number(message):
    """пользовательский ввод
    """
    number = None
    while number is None:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else None
    return number


def decimal_to_binary_conversion(number):
    """преобразование десятичного числа в двоичное
    """
    binary_number = str(0) if number == 0 else str()
    while number != int():
        binary_number += str(number % 2)
        number = int(number / 2)
    return binary_number[::-1]  # разворот строки


MESSAGE_FOR_USER = 'Please enter a natural number -> '
number = user_input_number(f'{MESSAGE_FOR_USER}')
binary_number = decimal_to_binary_conversion(number)
print(f'{number} -> {binary_number}')
