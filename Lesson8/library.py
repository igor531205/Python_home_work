def display_the_phone_book(filename: str, fields: list):
    """Выводит телефонный справочник.
    :param filename: Имя файла.
    :param fields: Названия полей для вывода.
    """

    data = read_csv(filename, len(fields))

    view_list_contact(fields, data)


def find_contact(filename: str, fields: list, number: int):
    """Выводит контакт из справочника по ФИО.
    :param filename: Имя файла.
    :param fields: Названия полей для вывода.
    :param number: Номер поля из fields для поиска.
    """

    data = read_csv(filename, len(fields))

    MESSAGE_FOR_USER = f'Please enter "{fields[number]}" to find contact in phone book -> '
    name = user_input_string(MESSAGE_FOR_USER)

    contact = list(filter(lambda item: item[number] == name, data))

    view_list_contact(fields, contact)


def add_contact(filename: str, fields: list):
    """Добавляет контакт в справочник.
    :param filename: Имя файла.
    :param fields: Названия полей для вывода.
    """

    write_csv(filename, input_contact(fields), 'a')


def remove_contact_from_phone_book(filename: str, fields: list, number: int):
    """Удаляет контакт из справочника.
    :param filename: Имя файла.
    :param fields: Названия полей для вывода.
    :param number: Номер поля из fields для поиска.
    """

    MESSAGE_FOR_USER =\
        f'Please enter "{fields[number]}" to remove contact in phone book -> '
    name = user_input_string(MESSAGE_FOR_USER)

    if remove_line_in_file(filename, fields, name):
        print(f'Contact {name} remove in phone book')


def update_contact_in_phone_book(filename: str, fields: list, number: int):
    """Обновляет контакт в справочнике.
    :param filename: Имя файла.
    :param fields: Названия полей для вывода.
    :param number: Номер поля из fields для поиска.
    """

    MESSAGE_FOR_USER =\
        f'Please enter "{fields[number]}" to update contact in phone book -> '
    name = user_input_string(MESSAGE_FOR_USER)

    if remove_line_in_file(filename, fields, name):
        print(f'Please update contact "{name}" in phone book!')
        write_csv(filename, input_contact(fields), 'a')


def save_phone_book_to_txt_file(filename_read: str, filename_write: str, fields: list):
    """Сохраняет справочник в файл.
    :param filename_read: Имя файла для чтения.
    :param filename_write: Имя файла для записи.
    :param fields: Названия полей для вывода.
    """

    write_to_file(filename_write, fields, read_csv(filename_read, len(fields)))


def user_input_number(message: str, begin: int, end: int) -> int:
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :param begin: Начальное значение ввода.
    :param end: Конечное значение ввода.
    :return: Число.
    """

    number = int()
    while not (begin <= number <= end):

        string = input(f'{message}')

        number = int(string) if string.isdigit() else int()

    return number


def user_input_string(message: str) -> str:
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :return: Текст, введеный пользователем.
    """

    string = str()
    while not string:

        string = input(f'{message}')

    return string


def input_contact(fields: list) -> list:
    """Ввод контакта пользователем.
    :param fields: Названия полей для вывода.
    :return: Возвращает введенный контакт.
    """

    data = []
    for item in fields:

        MESSAGE_FOR_USER = f'Please enter "{item}" for write to phone book -> '
        data.append(user_input_string(MESSAGE_FOR_USER))
    return data


def remove_line_in_file(filename: str, fields: list, find: str):
    """Удаляет строчку в файле.
    :param filename: Имя файла.
    :param fields: Названия полей для вывода.
    :param find: Слово для поиска строки и удаления.
    """

    remove_line = False
    data = []
    for line in read_csv(filename, len(fields)):
        if not find in line:
            data.append(line)
        else:
            remove_line = True

    with open(filename, 'w', encoding='utf-8') as new:
        new.write('')
    for line in data:
        write_csv(filename, line, 'a')

    return remove_line


def read_csv(filename: str, length_column: int) -> list:
    """Читает данные из файла.
    :param filename: Имя файла.
    :return: Список полученных данных.
    """

    data = []
    with open(filename, 'r', encoding='utf-8') as phonebook:

        for line in phonebook:
            temp = line.strip().split(',')

            if len(temp) == length_column:
                data.append(temp)

    return data


def write_csv(filename: str, data: list, mode: str):
    """Записывает в файл.
    :param filename: Имя файла.
    :param data: Информация для записи в файл.
    :param mode: Режим для записи в файл.
    """

    with open(filename, mode) as data_write:
        data_write.write(','.join(data) + '\n')


def write_to_file(filename: str, fields: list, contacts: list):
    """Записывает в файл.
    :param filename: Имя файла.
    :param fields: Названия полей для записи.
    :param contacts: Информация для записи в файл.
    """

    import json

    with open(filename, 'w', encoding='utf-8') as data_write:
        for item in contacts:
            data_write.writelines(json.dumps(dict(zip(fields, item))) + '\n')


def view_list_contact(fields: list, contacts: list):
    """Выводит список контактов.
    :param fields: Названия полей для вывода.
    :param contacts: Список контактов для вывода.
    """

    frame = [f'--{"-"*30}--' for _ in fields]

    print(*frame, sep=str())

    print(*[f'| {item:<30} |' for item in fields], sep=str())

    print(*frame, sep=str())

    for line in contacts:
        print(*[f'| {item:<30} |' for item in line], sep=str())

    print(*frame, sep=str())
