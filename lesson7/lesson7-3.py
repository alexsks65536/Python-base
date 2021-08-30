'''
    Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт,
    который собирает все шаблоны в одну папку templates, например:
    |--my_project
       ...
      |--templates
       |   |--mainapp
       |   |  |--base.html
       |   |  |--index.html
       |   |--authapp
       |      |--base.html
       |      |--index.html
    Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
    (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
    например, во фреймворке django.
'''
from os import path, walk, listdir
import shutil

folder_list = 'my_project'
temp_folder = 'templates'
try:
    for folder, directories, files in walk(folder_list):
        if temp_folder in directories and folder != folder_list:
            for entry in listdir(path.join(folder, temp_folder)):
                shutil.copytree(path.join(folder, temp_folder, entry), path.join(folder_list, temp_folder, path.basename(folder)))

except FileExistsError:
    print(f"Можно работать с {temp_folder}!")