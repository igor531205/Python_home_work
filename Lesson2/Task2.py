# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N. Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def user_input_number(message):
    '''пользовательский ввод'''
    ZERRO_NUMBER = 0
    number = ZERRO_NUMBER
    while not number:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else ZERRO_NUMBER
    return number


def list_product_of_numbers_from_one_to_number(number):
    '''список произведений чисел от 1 до number'''
    ONE_NUMBER = 1
    product_of_numbers = ONE_NUMBER
    list_product_of_numbers = list()
    for current_number in range(ONE_NUMBER, number + ONE_NUMBER):
        product_of_numbers *= current_number
        list_product_of_numbers.append(product_of_numbers)
    return list_product_of_numbers


MESSAGE_FOR_USER = 'Please enter a natural number -> '
number = user_input_number(f'{MESSAGE_FOR_USER}')
list_product_of_numbers = list_product_of_numbers_from_one_to_number(number)
print(f'{list_product_of_numbers}')
