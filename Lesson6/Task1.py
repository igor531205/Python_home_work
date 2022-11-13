# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# lambda, filter, zip, enumerate

def user_input_number(message, begin, end) -> int():
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :param begin: Начальное значение ввода.
    :param end: Конечное значение ввода.
    :return: Натуральное число, введеное пользователем.
    """
    number = int()
    while not (begin <= number <= end):
        string = input(f'{message}')
        number = int(string) if string.isdigit() else int()
    return number


def days_of_week() -> dict():
    """
    Создает список дней недели.
    :return: Список дней недели.
    """
    days_name = ['monday', 'tuesday', 'wednesday',
                 'thursday', 'friday', 'saturday', 'sunday']
    return dict(enumerate(days_name, start=1))


def is_weekends(day: int()) -> bool():
    """
    Проверяет, является ли день выходным.
    :param day: День недели.
    :return: True/False.
    """
    SATURDAY = 6
    SUNDAY = 7
    weekends = dict(filter(lambda item: item[0] in (SATURDAY, SUNDAY),
                           days_of_week().items()))
    if day in weekends.keys():
        return True
    return False


MONDAY = 1
SUNDAY = 7
MESSAGE_FOR_USER = \
    f'Please enter the day of week: for {MONDAY} to {SUNDAY} -> '
number_of_day = user_input_number(MESSAGE_FOR_USER, MONDAY, SUNDAY)
day_of_week, name_of_day = zip(
    *filter(lambda item: item[0] == number_of_day, days_of_week().items()))
string = 'is weekend' if is_weekends(number_of_day) else 'is not weekend'
print(f'Day {day_of_week[0]} "{name_of_day[0]}" {string}')
