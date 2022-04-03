"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы
с юникод: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

# данные в виде словаря, для записи в файл формата YAML
data_dic = {'100€': [1, 2, 3, 4],
            '200€': 8000,
            '300€': {'first': [1, 2, 3, 4],
                     'second': 800, }
            }


def write_dict_to_yaml(dic, file):
    """
    Функция для сохранение данных в файле YAML-формата
    :param dic:
    :param file:
    :return:
    """
    with open(file, 'w', encoding='utf-8') as f_n:
        yaml.dump(dic, f_n, default_flow_style=False, allow_unicode=True)

    with open(file, 'r', encoding='utf-8') as f_n:
        f_n_content = yaml.safe_load(f_n)
    print(f_n_content == dic)
    print(dic)
    print(f_n_content)


if __name__ == "__main__":
    write_dict_to_yaml(data_dic, 'file.yaml')
