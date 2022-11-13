# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

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


def list_of_prime_factors_of_number(number):
    """Находит список простых множителей числа.
    :param number: Число, для поиска простых множителей.
    :return: Cписок простых множителей числа.
    """
    list_of_prime_factors = [1 if not number else 0]
    if number > 0:
        list_of_prime_factors.append(1 if number == 1 else 0)
        if number > 1:
            for prime_number in range(2, number + 1):
                count_prime_number = int()
                while not number % prime_number:
                    count_prime_number += 1
                    number = number / prime_number
                list_of_prime_factors.append(count_prime_number)
                if number == 1:
                    break
    return list_of_prime_factors


def print_list_of_prime_factors_of_number(list_of_prime_factors):
    """Выводит на экран список простых множителей числа.
    :param list_of_prime_factors: Cписок простых множителей числа.
    """
    for prime_number in range(len(list_of_prime_factors)):
        if list_of_prime_factors[prime_number]:
            print(f'{prime_number}^{list_of_prime_factors[prime_number]}')


MESSAGE_FOR_USER = 'Please enter a natural number -> '
number_from_user = user_input_number(MESSAGE_FOR_USER)
list_of_prime_factors = list_of_prime_factors_of_number(number_from_user)
print(f'List of prime factors of number {number_from_user} ->')
print_list_of_prime_factors_of_number(list_of_prime_factors)
