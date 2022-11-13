# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def user_input_number(message):
    '''пользовательский ввод'''
    ZERRO_NUMBER = 0
    number = ZERRO_NUMBER
    while not number:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else ZERRO_NUMBER
    return number


def write_numbers_to_file(path, limit):
    '''запись двух случайных индексов в файл'''
    with open(path, 'w') as data:
        data.writelines(f'{randint(0, limit * 2)}\n')
        data.writelines(f'{randint(0, limit * 2)}\n')


def create_list_of_numbers(size):
    '''создание списка с числами'''
    list_of_numbers = list()
    for item in range(-size, size + 1):
        list_of_numbers.append(item)
    return list_of_numbers


def read_numbers_in_file(path):
    '''чтение индексов из файла'''
    numbers_in_file = list()
    data = open(path, 'r')
    for line in data:
        numbers_in_file.append(int(line[:-1]))
    data.close()
    return numbers_in_file


def product_on_accepted_positions_of_elements(list_of_numbers, positions):
    '''произведение элементов на указанных позициях'''
    POSITION_EMPTY = 0
    START_FOR_PRODUCT = 1
    product = START_FOR_PRODUCT if positions else POSITION_EMPTY
    for position in positions:
        product *= list_of_numbers[int(position)]
        print(f'{position} : {list_of_numbers[int(position)]}')
    return product


MESSAGE_FOR_USER = 'Please enter a natural number -> '
size = user_input_number(f'{MESSAGE_FOR_USER}')
PATH = 'file.txt'
write_numbers_to_file(PATH, size)
list_of_numbers = create_list_of_numbers(size)
print(f'{list_of_numbers}')
positions_in_file = read_numbers_in_file(PATH)
product_of_elements = product_on_accepted_positions_of_elements(
    list_of_numbers, positions_in_file)
print(f'{product_of_elements}')
