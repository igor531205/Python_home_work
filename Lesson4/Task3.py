# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

from random import randint


def user_input_number(message):
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :return: Число, введеное пользователем.
    """
    number = None
    while number is None:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else None
    return number


def create_list_of_random_numbers(list_lenght):
    """Создание списка случайных чисел.
    :param list_lenght: Длина списка случайных чисел.
    :return: Список случайных чисел.
    """
    list_of_random_numbers = list()
    for _ in range(list_lenght):
        list_of_random_numbers.append(randint(0, 9))
    return list_of_random_numbers


def removing_dentical_numbers_from_list(list_of_numbers):
    """Удаление одинаковых чисел из листа.
    :param list_of_numbers: Список чисел.
    :return: Список неповторяющихся чисел.
    """
    list_of_dentical_numbers = list()
    for current_element in range(len(list_of_numbers)):
        for other_element in range(len(list_of_numbers)):
            if current_element == other_element:
                continue
            if list_of_numbers[current_element] == \
                    list_of_numbers[other_element]:
                list_of_dentical_numbers.append(
                    list_of_numbers[current_element])
                break
    for current_element in list_of_dentical_numbers:
        if current_element in list_of_numbers:
            list_of_numbers.remove(current_element)
    return list_of_numbers


MESSAGE_FOR_USER = 'Please enter a natural number -> '
number_from_user = user_input_number(MESSAGE_FOR_USER)
list_of_random_numbers = create_list_of_random_numbers(number_from_user)
print(f'List of random numbers -> {list_of_random_numbers}')
list_of_non_repeating_numbers = removing_dentical_numbers_from_list(
    list_of_random_numbers)
print(f'List of non-repeating elements -> {list_of_non_repeating_numbers}')
