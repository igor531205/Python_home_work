# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# map

from random import randint


def user_input_number(message) -> int():
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :return: Натуральное число, введеное пользователем.
    """
    number = int()
    while not number:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else int()
    return number


def create_list_of_numbers(number) -> list():
    """Создание списка со случайными числами.
    :param number: Длина списка.
    :return: Список со случайными числами.
    """
    def products_of_numbers(number):
        product_of_numbers = int(1)
        while number:
            product_of_numbers *= number
            number -= 1
        return product_of_numbers

    return list(map(products_of_numbers, range(1, number + 1)))


MESSAGE_FOR_USER = f'Please enter a natural number -> '
user_number = user_input_number(MESSAGE_FOR_USER)
list_of_numbers = create_list_of_numbers(user_number)
print(f'{user_number} => {list_of_numbers}')
