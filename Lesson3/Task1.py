# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def create_list_of_numbers():
    """создание списка со случайными числами    
    """
    list_of_numbers = list()
    size = randint(2, 10)
    for _ in range(size):
        list_of_numbers.append(randint(1, 9))
    return list_of_numbers


def create_list_items_in_odd_positions(list_of_numbers):
    """создание списка с числами стоящими на нечётных позициях
    """
    list_items_in_odd_positions = list()
    START_ELEMENT = 1
    STEP = 2
    end_element = len(list_of_numbers)
    for item in range(START_ELEMENT, end_element, STEP):
        list_items_in_odd_positions.append(list_of_numbers[item])
    return list_items_in_odd_positions


def sum_elements_of_list(list_of_numbers):
    """сумма элементов списка
    """
    sum_elements = int()
    for item in list_of_numbers:
        sum_elements += item
    return sum_elements


list_of_numbers = create_list_of_numbers()
list_items_in_odd_positions = create_list_items_in_odd_positions(
    list_of_numbers)
sum_elements = sum_elements_of_list(list_items_in_odd_positions)
print(f'{list_of_numbers} -> {list_items_in_odd_positions} -> \
{sum_elements}')
