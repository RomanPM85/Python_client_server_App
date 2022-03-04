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

import csv
import re
import chardet


#  Вводные данные (список файлов, в неизвестной кодировке)
list_input_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(files):
    """
    Функция, которая получаем из аргумента files список файлов, определяет для каждого файла кодировку, читает
    файл и с помощью регулярных выражений извлекает значения параметров для переменной main_data.
    :param files:
    :return: main_data
    """
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
        content = content.decode(chardet.detect(content)['encoding'])
        os_prod_list = file, re.findall(r'Изготовитель системы:\s+(\w+)', content)[0].strip()
        os_name_list = file, re.findall(r'Название ОС:\s+([\w.\s]+)\n', content)[0].strip()
        os_code_list = file, re.findall(r'Код продукта:\s+([\w\-]+\w+)', content)[0].strip()
        os_type_list = file, re.findall(r'Тип системы:\s+([\w\-\w\s\w]+)', content)[0].strip()
        main_data.extend([[os_prod_list[1], os_name_list[1], os_code_list[1], os_type_list[1]]])
        print(main_data)
    return main_data


def write_to_csv(csv_file, input_files):
    """
    Функция, которая извлекает значения параметров из неизвестных файлов в неизвестной кодировке
    и сохраняет данные в указанном в аргументе файле.
    :param csv_file:
    :param input_files:
    :return:
    """

    to_write = get_data(input_files)
    with open(csv_file, 'w', encoding='utf-8', newline="") as main_data_file:
        md_writer = csv.writer(main_data_file, quoting=csv.QUOTE_ALL, quotechar="\"")
        md_writer.writerow(to_write[0])
        md_writer.writerows(to_write[1:], )
    return print(f'Данные записаны в файл: {csv_file}')


if __name__ == "__main__":
    write_to_csv('main.csv', list_input_files)
