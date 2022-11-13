# Задайте список из n чисел последовательности (1+1/n)**n и
# выведите на экран их сумму. Пример:
# - Для n = 6: {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3}

def user_input_number(message):
    '''пользовательский ввод'''
    ZERRO_NUMBER = 0
    number = ZERRO_NUMBER
    while not number:
        string = input(f'{message}')
        number = int(string) if string.isdigit() else ZERRO_NUMBER
    return number


def dictionary_of_sequence_of_numbers(number):
    '''список из n чисел последовательности (1+1/n)**n'''
    ONE_NUMBER = 1
    dictionary_of_sequence = dict()
    for current_number in range(ONE_NUMBER, number + ONE_NUMBER):
        dictionary_of_sequence[current_number] = round(
            (ONE_NUMBER + ONE_NUMBER / current_number) ** current_number)
    return dictionary_of_sequence


MESSAGE_FOR_USER = 'Please enter a natural number -> '
number = user_input_number(f'{MESSAGE_FOR_USER}')
ictionary_of_sequence = dictionary_of_sequence_of_numbers(number)
print(f'{ictionary_of_sequence}')
