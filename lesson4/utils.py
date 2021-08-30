#4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

from datetime import date
from requests import get, utils

value = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rates(code_val):
    finder = value.split("<Valute ID=")
    day, month, year = finder[0].split('"')[-4].split(".")

    for n in finder:
        if code_val.upper() in n:
            print(date(year=int(year), month=int(month), day=int(day)), end=": ")
            return float(n.replace("/", "").split("<Value>")[-2].replace(",", "."))

if __name__== "__main__":
    print(currency_rates("USd"))
    print(currency_rates("euR"))