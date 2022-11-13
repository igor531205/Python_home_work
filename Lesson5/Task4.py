# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_compression(string):
    """Сжимает данные.
    :param string: Строка для сжатия.
    :return: Сжатые данные.
    """
    compression = ''
    previous_char = ''
    count = 1
    if not string:
        return ''
    for char in string:
        if char != previous_char:
            if previous_char:
                compression += str(count) + previous_char
            count = 1
            previous_char = char
        else:
            count += 1
    else:
        compression += str(count) + previous_char
    return compression


string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(rle_compression(string))
