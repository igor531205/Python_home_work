# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def game_candy():
    """Игра с конфетами.
    """

    def user_input_number(message, begin, end):
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

    def bot_input_number(message, candy, begin, end):
        """Ввод от бота.
        :param message: Сообщение пользователю.
        :param candy: Количество конфет.
        :param begin: Начальное значение ввода.
        :param end: Конечное значение ввода.
        :return: Число.
        """
        if candy > end:
            number = randint(begin, end)
        else:
            number = end
        print(f'{message} {number}')
        return number

    def took_candy(name, candy, min_candy, max_candy):
        """Взять конфет.
        :param name: Имя игрока.
        :param candy: Количество конфет.
        :param min_candy: Мин, что может взять игрок.
        :param max_candy: Макс, что может взять игрок.
        :return: Количество взятых конфет.
        """
        message = f'{name} enter how many candy you want to take from '\
            + f'{min_candy} to {max_candy} -> '
        took = bot_input_number(message, candy, min_candy, max_candy) if name == "Bot"\
            else user_input_number(message, min_candy, max_candy)
        return took

    def game_loop(players):
        """Игровой цикл.
        :param players: Количество других игроков (не считая пользователя).
        :return: Имя победителя.
        """
        candy_left = 2021
        print(f'{candy_left} candy on the table.')
        move_other_player = True if randint(0, 2) else False
        players_names = [f'Player 1', f'{"Player 2" if players else "Bot"}']
        print(f'{players_names[move_other_player]} goes fist')
        MIN_CANDY, MAX_CANDY = 1, 28
        candy_counter = [0, 0]

        while candy_left > 0:
            took = took_candy(players_names[move_other_player],
                              candy_left, MIN_CANDY,
                              MAX_CANDY if candy_left >= MAX_CANDY else candy_left)
            candy_counter[move_other_player] += took
            candy_left -= took
            print(f'{players_names[move_other_player]} took {took} candy, '
                  + f'now he has {candy_counter[move_other_player]} candy. '
                  + f'{candy_left} candy left on the table.')
            if candy_left:
                move_other_player = not move_other_player
        return players_names[move_other_player]

    WELCOME_MESSAGE = f'Hello, this is Candy 2021 Game'
    print(f'{WELCOME_MESSAGE}')
    MIN_PLAYERS = 1
    MAX_PLAYERS = 2
    MESSAGE_FOR_USER = \
        f'Enter the number of players from {MIN_PLAYERS} to {MAX_PLAYERS} -> '
    other_players = \
        user_input_number(MESSAGE_FOR_USER, MIN_PLAYERS, MAX_PLAYERS) - 1
    player_win = game_loop(other_players)
    print(f'{player_win} win!')


game_candy()
