'''
Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''
import yaml
import os
with open('config.yaml') as config_list:
    config = yaml.safe_load(config_list)

def start_dirs(val, prefix=""):
    for dir, dir_include in val.items():
        folder = os.path.join(prefix, dir)
        os.makedirs(folder, exist_ok=True)
        if isinstance(dir_include, dict):
            start_dirs(dir_include, folder)
        else:
            for s in dir_include:
                if isinstance(s, dict):
                    start_dirs(s, folder)
                elif isinstance(s, str):
                    with open(os.path.join(folder, f'{s}'), 'w') as _temp:
                        pass

start_dirs(config)