# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def create_list_of_numbers():
    """создание списка со случайными числами
    """
    list_of_numbers = list()
    size = randint(1, 10)
    for _ in range(size):
        list_of_numbers.append(randint(1, 9))
    return list_of_numbers


def create_list_of_pairs_product_of_numbers(list_of_numbers):
    """создание списка с произведением пар чисел списка
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    """
    list_of_pairs_product_of_numbers = list()
    length = len(list_of_numbers)
    # расчет середины списка с округлением до большего числа
    end_element = int(length / 2) if not (length % 2) else int(length / 2 + 1)
    for item in range(end_element):
        # расчет произведения пар чисел
        product_of_numbers = \
            list_of_numbers[item] * list_of_numbers[-(item + 1)]
        list_of_pairs_product_of_numbers.append(product_of_numbers)
    return list_of_pairs_product_of_numbers


list_of_numbers = create_list_of_numbers()
list_of_pairs_product_of_numbers = \
    create_list_of_pairs_product_of_numbers(list_of_numbers)
print(f'{list_of_numbers} -> {list_of_pairs_product_of_numbers}')
