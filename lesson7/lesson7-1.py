'''
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
'''
import os

dir_name = 'my_project'
dir_name_2 = 'settings', 'mainapp', 'adminapp', 'authapp'

os.makedirs(dir_name, exist_ok=True)

for i in dir_name_2:
    dir_ = os.path.join(dir_name, i)
    os.makedirs(dir_, exist_ok=True)
'''
# вариант из урока
p_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, value in p_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
'''


