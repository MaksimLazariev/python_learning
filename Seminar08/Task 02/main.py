"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект и достучаться до списка,
который и нужно пополнять, а потом сохранять все в файл
"""

import json


# Функция добавления заказов в файл
def write_order_to_json(item, quantity, price, buyer, date):
    file = 'orders.json'
    # Считываем данные из файла в словарь
    with open(file, encoding='utf-8') as f_n:
        json_dict = json.load(f_n)

        # Записываем введенные данные в словарь
        json_dict['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    # Пишем данные из словаря в файл
    with open(file, 'w', encoding='utf-8') as f_w:
        json.dump(json_dict, f_w, indent=4, ensure_ascii=False)


# Примеры для проверки
if __name__ == "__main__":
    write_order_to_json('Монитор', 2, 5000, 'Иванов', '08.02.2023')
    write_order_to_json('HDD', 5, 3000, 'Петров', '15.02.2023')
