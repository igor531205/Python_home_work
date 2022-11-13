# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

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
    """Создает список случайных чисел.
    :param list_lenght: Длина списка случайных чисел.
    :return: Список случайных чисел.
    """
    list_of_random_numbers = list()
    for _ in range(list_lenght):
        list_of_random_numbers.append(randint(0, 9))
    return list_of_random_numbers


def create_polynomial(list_of_numbers):
    """Формирует многочлен.
    :param list_of_numbers: Список чисел.
    :return: Многочлен.
    """
    polynomial = [(f'{list_of_numbers[i]}*x^{i}' if i > 1 else
                  f'{list_of_numbers[i]}*x' if i else f'{list_of_numbers[i]}')
                  for i in range(len(list_of_numbers)) if list_of_numbers[i]]
    polynomial.reverse()
    polynomial = f'{" + ".join(polynomial)} = 0' if len(polynomial) > 1 else str()
    return polynomial


def write_to_file(file_name, data):
    """Записывает в файл.    
    :param file_name: Имя файла.
    :param data: Информация для записи в файл.
    """
    with open(file_name, 'w') as data_write:
        data_write.write(f'{data}')


if __name__ == "__main__":
    MESSAGE_FOR_USER = 'Please enter a natural number -> '
    number_from_user = user_input_number(MESSAGE_FOR_USER)
    list_of_random_numbers = create_list_of_random_numbers(number_from_user)
    polynomial = create_polynomial(list_of_random_numbers)
    FILE_NAME = 'file.txt'
    write_to_file(FILE_NAME, polynomial)
