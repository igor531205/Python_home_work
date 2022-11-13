# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (негафибоначчи).
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from math import pow


def user_input_number(message):
    """пользовательский ввод
    """
    number = int()
    while not number:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else int()
    return number


def negafibonacci(number):
    """список чисел Фибоначчи, в том числе для отрицательных индексов 
    (негафибоначчи)
    """
    return list(fibonacci(num) for num in range(-number, number + 1))


def fibonacci(number):
    """поиск числа Фибоначчи, по индексу
    """
    if number >= 0:
        range_numbers = range(number+1)
        list_numbers = [0, 1]
        for item in range_numbers[2:]:
            list_numbers.append(list_numbers[item-1] + list_numbers[item-2])
        return list_numbers[number]
    else:
        number = -(number-1)
        range_numbers = range(number+1)
        list_numbers = [1, 0]
        for item in range_numbers[2:]:
            list_numbers.append(list_numbers[item-2] - list_numbers[item-1])
        list_numbers.reverse()
    return list_numbers[0]


MESSAGE_FOR_USER = 'Please enter a natural number -> '
number = user_input_number(f'{MESSAGE_FOR_USER}')
print(negafibonacci(number))
