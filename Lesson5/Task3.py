# Создайте программу для игры в "Крестики-нолики".

def game_tic_tac_toe():
    """Игра крестики-нолики.
    """
    WELCOME_MESSAGE = f'Hello, this is tic-tac-toe game'
    print(f'{WELCOME_MESSAGE}')
    game_board = list(range(1, 10))
    move_counter, player = 0, 0
    while move_counter < 9:
        draw_board(game_board)
        take_input(player, game_board)
        if check_win(game_board):
            draw_board(game_board)
            print(
                f'''Player №{player + 1} {'"O"' if player else '"X"'} win!''')
            break
        player = not player
        move_counter += 1
    else:
        print("Draw game!")


def draw_board(game_board):
    """Рисует игровое поле.
    :param game_board: Список полей.
    """
    print(f'{"-" * 13}')
    for i in range(3):
        print(
            f'| {game_board[0+i*3]} | {game_board[1+i*3]} | {game_board[2+i*3]} |')
        print(f'{"-" * 13}')


def take_input(player, game_board):
    """Запрашивает ввод от игрока.
    :param player: Номер игрока.
    :param game_board: Список полей.
    """
    BEGIN = 1
    END = 9
    field = int()
    while not (BEGIN <= field <= END):
        string = input(
            f'''Move Player №{player + 1} {'"O"' if player else '"X"'} -> ''')
        field = int(string) if string.isdigit() else int()
        if BEGIN <= field <= END:
            if (str(game_board[field-1]) not in "XO"):
                game_board[field-1] = 'O' if player else 'X'
            else:
                print(f'This cell is occupied!')
                field = int()
        else:
            print(f'Invalid input.')


def check_win(game_board):
    """Проверка на победу.
    :param game_board: Список полей.
    """
    WIN_FIELD = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for field in WIN_FIELD:
        if game_board[field[0]] == game_board[field[1]] == game_board[field[2]]:
            return game_board[field[0]]
    return False


game_tic_tac_toe()
