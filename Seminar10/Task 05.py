"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

sites = ['yandex.ru', 'youtube.com']

for site in sites:
    args = ['ping', site]
    sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in sub_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))