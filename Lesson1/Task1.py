# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным. Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

def is_weekends(day):
    MONDAY = 1
    SATURDAY = 6
    SUNDAY = 7
    if SATURDAY <= day <= SUNDAY:
        return f'Yes'
    elif MONDAY <= day < SATURDAY:
        return f'No'
    else:
        return f'Error to enter day'


message_for_input = f'Enter day of weak - '
day_of_weak = int(input(message_for_input))
message = '-> ' + is_weekends(day_of_weak)
print(message)
