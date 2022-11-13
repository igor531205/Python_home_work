# Реализуйте алгоритм перемешивания списка.

from random import randint


def create_list_of_numbers():
    '''создание списка со случайными числами'''
    list_of_numbers = list()
    size = randint(1, 10)
    for item in range(-size, size + 1):
        list_of_numbers.append(item)
    return list_of_numbers


def list_shuffling(list_of_numbers):
    '''перемешивание списка'''
    shuffled_list = list()
    position = len(list_of_numbers)
    for item in list_of_numbers:
        shuffled_list.insert(position, item)
        position -= 1
    return shuffled_list


list_of_numbers = create_list_of_numbers()
print(f'{list_of_numbers}')
print(f'{list_shuffling(list_of_numbers)}')
