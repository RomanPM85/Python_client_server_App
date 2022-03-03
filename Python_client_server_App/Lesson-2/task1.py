"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
получение данных через вызов функции get_data(), а также сохранение подготовленных данных в
соответствующий CSV-файл; Проверить работу программы через вызов функции write_to_csv().
"""
import re

from chardet import detect


# Вводные данные
input_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
list_encoding = []  # список кодировки файлов
os_prod_list = []  # «Изготовитель системы»
os_name_list = []  # список «Название ОС»
os_code_list = []  # список «Код продукта»
os_type_list = []  # список «Тип системы»


def get_data(files):
    """
    Функция, которая определяет кодировку файлов, читает файл и дополнительно возвращает
    список кодировок.
    :param files:
    :return: list_encoding
    """

    for file in files:
        # узнаём кодировку неизвестного нам файла
        with open(file, 'rb') as f:
            content = f.read()
        encoding = detect(content)['encoding']
        print('encoding: ', encoding)
        list_encoding.append(encoding)

        # открываем файл в известной нам кодировке
        with open(file, encoding=encoding) as f_n:
            for el_str in f_n:
                print(el_str, end='')
            print()
            print('-' * 70)

            # result = []
            # for line in f_n.readiness():
            #     result += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)
            #     print(result)


def write_to_csv():
    pass


if __name__ == "__main__":
    get_data(input_files)
    # print(list_encoding)
