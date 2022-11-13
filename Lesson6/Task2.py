# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]
# lambda, map, list comprehension

from random import randint


def create_list_of_numbers() -> list():
    """Создание списка со случайными числами.
    :return: Список со случайными числами.
    """
    return [randint(1, 9) for _ in range(1, randint(3, 9))]


def product_pairs_of_numbers(list_of_numbers) -> list():
    """создание списка с произведением пар чисел списка
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    :param list_of_numbers: Список с числами.
    :return: Список с роизведением пар чисел.
    """
    lenght_list_of_numbers = int((len(list_of_numbers) + 1)/2)
    return list(map(
        lambda item: list_of_numbers[item] * list_of_numbers[-(item + 1)],
        range(lenght_list_of_numbers)))


list_of_numbers = create_list_of_numbers()
print(f'{list_of_numbers} => {product_pairs_of_numbers(list_of_numbers)}')
