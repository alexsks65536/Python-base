'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
 и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError
 #>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном
случае использовать функцию re.compile()?
'''
import re

class email_error(Exception):
    def __init__(self, text):
        self.txt = text

email_list = ['whitesnake@yandex.ru', 'someone@geekbrainsru', 'someone @geekbrains.ru']

for email in email_list:

    try:
        if not re.findall(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$', email):
            raise email_error("You give wrong e-mail!")
    except ValueError:
        print("Error type of value!")
    except email_error as mr:
        print(mr)
    else:
        em = re.split(r'@', email)
        address = {'username': em[0], 'domain': em[1]}
        print(address)

