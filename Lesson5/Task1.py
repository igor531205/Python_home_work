# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def user_input_string(message):
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :return: Текст, введеный пользователем.
    """
    string = str()
    while not string:
        string = input(f'{message}')
    return string


def removes_words_from_text(text, string):
    """Удаляет слова из текста.
    :param text: Текст для корректировки.
    :param string: Строка для удаления содержащих ее слов.
    :return: Скорректированный текст.
    """
    list_of_words = list(filter(lambda word: string not in word, text.split()))
    return f' '.join(list_of_words)


MESSAGE_FOR_USER = 'Please enter a text with and without words containing "абв" -> '
user_input = user_input_string(MESSAGE_FOR_USER)
STRING_TO_DELETE_WORD = 'абв'
print(
    f'Corrected text -> {removes_words_from_text(user_input, STRING_TO_DELETE_WORD)}')
