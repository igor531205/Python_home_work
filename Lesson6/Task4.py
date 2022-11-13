# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# enumerate, list comprehension

from random import randint


def create_list_of_numbers() -> list():
    """Создание списка со случайными числами.
    :return: Список со случайными числами.
    """
    return [randint(1, 9) for _ in range(randint(3, 9))]


def create_list_of_numbers_in_odd_positions(list_of_numbers) -> list():
    """создание списка с числами стоящими на нечётных позициях.
    :param list_of_numbers: Список с числами.
    :return: Список с числами стоящими на нечётных позициях.
    """
    return [number for key, number in enumerate(list_of_numbers) if key % 2 != 0]


def sum_elements_of_list(list_of_numbers):
    """сумма элементов списка
    """
    return sum(list_of_numbers)


list_of_numbers = create_list_of_numbers()
list_of_numbers_in_odd_positions = \
    create_list_of_numbers_in_odd_positions(list_of_numbers)
sum_elements = sum_elements_of_list(list_of_numbers_in_odd_positions)
print(f'{list_of_numbers} => summa {list_of_numbers_in_odd_positions} = {sum_elements}')
