# Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл, содержащий
# сумму многочленов.

from Task4 import create_list_of_random_numbers
from Task4 import create_polynomial
from Task4 import write_to_file


def create_files_with_polynomials(number):
    """Записывает в файл многочлен.    
    :param number: Количество файлов.
    """
    LENGHT_POLYNOMIAL = 5
    for i in range(number):
        file_name = f'file{i if i else ""}.txt'
        write_to_file(file_name, create_polynomial(
            create_list_of_random_numbers(LENGHT_POLYNOMIAL)))


def read_in_file(file_name):
    """Считывает данные из файла.    
    :param file_name: Имя файла.
    :return: Считанные данные.
    """
    data = str()
    data_read = open(file_name, 'r')
    data = data_read.read()
    data_read.close()
    return data


def read_polynomials_in_file(number):
    """Считывает многочлен из файла.    
    :param number: Количество файлов.
    """
    data = list()
    for i in range(number):
        file_name = f'file{i if i else ""}.txt'
        string = read_in_file(file_name)
        dict_of_polynomial = dict()
        if string:
            find_end = string.find(' = 0') \
                if string.find(' = 0') >= 0 else len(string)
            string = string[:find_end]
            list_of_polynomial = [polynom for polynom in string.split(' + ')]
            for polynom in list_of_polynomial:
                if polynom.find('*x^') >= 0:
                    dict_of_polynomial[int(polynom[int(polynom.find('*x^')) + len('*x^'):])] = \
                        int(polynom[:int(polynom.find('*x^'))])
                elif polynom.find('*x') >= 0:
                    dict_of_polynomial[1] = \
                        int(polynom[:int(polynom.find('*x'))])
                else:
                    dict_of_polynomial[0] = int(polynom)
        data.append(dict_of_polynomial)
    return data


def sum_of_polynomials(list_of_polynomials):
    """Суммирут многочлены из списка.    
    :param list_of_polynomials: Список многочленов.
    :return: Сумма многочленов.
    """
    def order_dic(dic):
        """Сортировка словаря.    
        """
        ordered_dic = {}
        keys = sorted(dic.keys())
        keys.reverse()
        for key in keys:
            ordered_dic[key] = dic[key]
        return ordered_dic

    dict_of_polynomial = dict()
    for polynom in list_of_polynomials:
        for x, koef in polynom.items():
            if not dict_of_polynomial.get(x):
                dict_of_polynomial[x] = polynom[x]
            else:
                dict_of_polynomial[x] += polynom[x]
    return order_dic(dict_of_polynomial)


def polynomial_to_string(dict_of_polynomial):
    """Формирует многочлен.
    :param dict_of_polynomial: Многочлен.
    :return: Многочлен строковый.
    """
    polynomial = [(f'{koef}*x^{x}' if x > 1 else
                  f'{koef}*x' if x else f'{koef}')
                  for x, koef in dict_of_polynomial.items()]
    polynomial = f'{" + ".join(polynomial)} = 0' if len(polynomial) > 1 else str()
    return polynomial


NUMBER_OF_FILES_TO_WRITE = 2
create_files_with_polynomials(NUMBER_OF_FILES_TO_WRITE)
dict_of_polynomial = read_polynomials_in_file(NUMBER_OF_FILES_TO_WRITE)
sum_of_polynomials = sum_of_polynomials(dict_of_polynomial)
string_of_polynomial = polynomial_to_string(sum_of_polynomials)
write_to_file(f'sum_of_polynom.txt', string_of_polynomial)
