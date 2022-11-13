def show_menu() -> int:
    """Меню выбора действия.    
    :return: Выбранное число.
    """
    MIN_CHOICE = 1
    MAX_CHOICE = 6
    MESSAGE_FOR_USER = (f''' {'"'*10} Main menu: {'"'*10}
                        \r 1. "Display the phone book"
                        \r 2. "Find a contact by full name"
                        \r 3. "Find a contact by phone number"
                        \r 4. "Add a contact to the phone book"
                        \r 5. "Save phone book in txt file"
                        \r 6. "Exit the program"
                        \r Enter menu item number -> ''')
    return user_input_number(MESSAGE_FOR_USER, MIN_CHOICE, MAX_CHOICE)


def display_the_phone_book(filename: str, fields: list):
    """Выводит телефонный справочник.
    :param filename: Имя файла.  
    :param fields: Названия полей для вывода.      
    """
    data = read_csv(filename)

    view_list_contact(fields, data)


def find_contact(filename: str, fields: list, number: int):
    """Выводит контакт из справочника по ФИО.
    :param filename: Имя файла.  
    :param fields: Названия полей для вывода.   
    """
    data = read_csv(filename)

    MESSAGE_FOR_USER = f'Please enter a "{fields[number]}" to find contact in phone book -> '
    name = user_input_string(MESSAGE_FOR_USER)

    contact = list(filter(lambda item: item[number] == name, data))

    view_list_contact(fields, contact)


def add_contact(filename: str, fields: list):
    data = []
    for item in range(3):
        MESSAGE_FOR_USER = f'Please enter a "{fields[item]}" for write to phone book -> '
        data.append(user_input_string(MESSAGE_FOR_USER))

    write_csv(filename, data)


def save_phone_book_in_txt_file(filename_read: str, filename_write: str, fields: list):
    """Сохраняет справочник в файл.
    :param filename_read: Имя файла для чтения.
    :param filename_write: Имя файла для записи.  
    :param fields: Названия полей для вывода.   
    """
    write_to_file(filename_write, fields, read_csv(filename_read))


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


def read_csv(filename: str) -> list:
    """Читает данные из файла.
    :param filename: Имя файла.  
    :return: Список полученных данных.   
    """
    data = []
    with open(filename, 'r', encoding='utf-8') as phonebook:
        for line in phonebook:
            temp = line.strip().split(',')
            if len(temp) == 3:
                data.append(temp)
    phonebook.close()
    return data


def write_csv(filename: str, data: list):
    """Записывает в файл.
    :param filename: Имя файла.  
    :param data: Информация для записи в файл.
    """
    with open(filename, 'a') as data_write:
        data_write.write('\n'+','.join(data))


def write_to_file(file_name: str, fields: list, contacts: list):
    """Записывает в файл.    
    :param file_name: Имя файла.
    :param fields: Названия полей для записи.
    :param contacts: Информация для записи в файл.
    """
    data = f'{"-"*90}\n{list_to_string(fields)}\n{"-"*90}\n'
    for item in contacts:
        data += f'{list_to_string(item)}\n'
    data += f'{"-"*90}\n'
    with open(file_name, 'w') as data_write:
        data_write.write(data)


def view_list_contact(fields: list, contacts: list):
    """Выводит список контактов.
    :param fields: Названия полей для вывода.    
    :param contacts: Список контактов для вывода.
    """
    print(f'{"-"*90}')
    print(f'{list_to_string(fields)}')
    print(f'{"-"*90}')
    for item in contacts:
        print(f'{list_to_string(item)}')
    print(f'{"-"*90}')


def list_to_string(data: list) -> str:
    """Подготавливает данные.    
    :param data: Список для преобразования в строку.
    :return: Строка с данными.
    """
    return f'| {data[0]:<30} | {data[1]:<20} | {data[2]:<30} |'
