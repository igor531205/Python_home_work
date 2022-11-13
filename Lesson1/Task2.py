# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_numbers(message):
    names = ['X', 'Y', 'Z']
    array = [False, False, False]
    for i in range(3):
        print_message = f'{message} {names[i]} - '
        array[i] = bool(input(print_message))
    return array


def check_predicate(array):
    predicate_one = not (array[0] or array[1] or array[2])
    predicate_two = not array[0] and not array[1] and not array[2]
    return predicate_one == predicate_two


predicates = input_numbers(f'Enter value')
print(f'Statement {check_predicate(predicates)}')
