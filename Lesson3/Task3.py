# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#lst = [1.1, 1.2, 3.1, 5, 10.01]
#lst = [round(val % 1, 2) for val in lst]
#rev_result = max(lst) - min(lst)


from random import randrange
from random import randint


def create_list_of_numbers():
    """создание списка со случайными числами
    """
    list_of_numbers = list()
    size = randint(2, 10)
    for _ in range(size):
        list_of_numbers.append(randrange(1, 1000)/100)
    return list_of_numbers


def search_max_fractional_part_of_elements(list_of_numbers):
    """поиск максимальной дробной части элементов
    """
    max_fractional_part = float()
    for item in list_of_numbers:
        # расчет дробной части
        fractional_part = round((item - int(item)), 2)
        if max_fractional_part < fractional_part:
            max_fractional_part = fractional_part
    return max_fractional_part


def search_min_fractional_part_of_elements(list_of_numbers):
    """поиск минимальной дробной части элементов
    """
    min_fractional_part = float(1)
    for item in list_of_numbers:
        # расчет дробной части
        fractional_part = round((item - int(item)), 2)
        if min_fractional_part > fractional_part:
            min_fractional_part = fractional_part
    return min_fractional_part


def difference_between_max_and_min_value(max_value, min_value):
    """разница между максимальным и минимальным значением
    """
    return round((max_value - min_value), 2)


list_of_numbers = create_list_of_numbers()
max_fractional_part_of_elements = \
    search_max_fractional_part_of_elements(list_of_numbers)
min_fractional_part_of_elements = \
    search_min_fractional_part_of_elements(list_of_numbers)
difference_between_value = \
    difference_between_max_and_min_value(
        max_fractional_part_of_elements, min_fractional_part_of_elements)
print(f'{list_of_numbers} -> {max_fractional_part_of_elements} - \
{min_fractional_part_of_elements} = {difference_between_value}')
