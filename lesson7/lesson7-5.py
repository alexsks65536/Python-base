'''
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
'''
import os
import django
import json

def folder_list():
    root_dir = django.__path__[0]
    django_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if size in django_files:
                django_files[size][0] += 1
                if ext not in django_files[size][1]:
                    django_files[size][1].append(ext)
            else:
                django_files[size] = [1, [ext]]
    result = {}

    for size, list_log in sorted(django_files.items()):
        result[size] = tuple(list_log)
        print(f'{size}: {tuple(list_log)}')

    folder_name = os.path.basename(os.getcwd()) + '_summary.json'
    with open(folder_name, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    folder_list()