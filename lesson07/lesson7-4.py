'''
    Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
     а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
    Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
    Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''
import os
import django
from collections import defaultdict

def folder_list():
    folder_root = django.__path__[0]
    list_of_files = defaultdict(int)
    for root, dirs, files in os.walk(folder_root):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            list_of_files[size] += 1

    for file_size, file_nums in sorted(list_of_files.items()):
        print(f'размер файлов, до - {file_size}, byte: {file_nums}')

folder_list()