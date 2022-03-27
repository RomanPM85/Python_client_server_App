"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


item_bd = ['Телефон', 'Ноутбук', 'Проектор', 'Монитор']
quantity_bd = [3, 2, 3, 4]
price_bd = [30000, 70000, 12000, 15000]
buyer_bd = ['Роман', 'Надежда', 'Игорь', 'Владимир']
date_bd = ['08.03.2022', '08.03.2022', '08.03.2022', '08.03.2022']


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f_n:
        dict_to_json = json.load(f_n)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w', encoding='utf-8') as f_w:
        json.dump(dict_to_json, f_w, indent=4)


if __name__ == "__main__":
    write_order_to_json(item_bd[0], quantity_bd[0], price_bd[0], buyer_bd[0], date_bd[0])
    write_order_to_json(item_bd[1], quantity_bd[1], price_bd[1], buyer_bd[1], date_bd[1])
    write_order_to_json(item_bd[2], quantity_bd[2], price_bd[2], buyer_bd[2], date_bd[2])
    write_order_to_json(item_bd[3], quantity_bd[3], price_bd[3], buyer_bd[3], date_bd[3])
