# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# list comprehension

from random import randint
from random import randrange


def create_list_of_numbers() -> list():
    """Создание списка со случайными числами.
    :return: Список со случайными числами.
    """
    return [randrange(1, 1000)/100 for _ in range(1, randint(3, 9))]


def difference_between_max_and_min_fractional_part(list_of_numbers) -> float():
    """Разница между максимальным и минимальным значением дробной части.
    :param list_of_numbers: Список с числами.
    :return: Список с роизведением пар чисел.
    """
    fractional_part = [item % 1 for item in list_of_numbers]
    return max(fractional_part) - min(fractional_part)


list_of_numbers = create_list_of_numbers()
fractional_part_of_list_of_numbers = \
    difference_between_max_and_min_fractional_part(list_of_numbers)
print(f'{list_of_numbers} => {fractional_part_of_list_of_numbers:0.2f}')
