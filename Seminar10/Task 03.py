"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''
(без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

"""
Решение.
При записи переменной words = [b'attribute', b'класс', b'функция', b'type']
сразу же возникает ошибка SyntaxError: bytes can only contain ASCII literal 
characters, т.е переменная байтового типа может содержать только ASCII символы.
Таким образом слова «класс» и «функция» невозможно записать с помощью 
маркировки b'.

Для того чтобы отловить такие значения создаем функцию is_ascii, которая 
проверяет, находится ли значения символов строки в ASCII или нет.
Если значения символов строки находятся вне ASCII, тогда принудительно вызываем 
ошибку BytesEncodingError
"""


# Создаем класс ошибки перевода в байтовый тип
class BytesEncodingError(Exception):
    pass


# Проверяем, находится ли строка в ASCII или нет (кириллица даст False)
def is_ascii(string):
    return all(ord(char) < 255 for char in string)


# Исходные слова
words = ['attribute', 'класс', 'функция', 'type']
byte_words = []

# Записываем слова в байтовом формате
for word in words:
    try:
        # Отлавливаем кириллицу
        if is_ascii(word):
            # Все хорошо, слово добавляем в список
            byte_words.append(bytes(word, 'utf-8'))
        else:
            # Иначе ошибка
            raise BytesEncodingError(word)
    except BytesEncodingError as error:
        print("Слово '{}' нельзя записать в ASCII".format(error))

# Печатаем получившийся список
for word in byte_words:
    print(
        "Тип {}, Содержимое {}, длина {}".format(type(word), word, len(word)))
