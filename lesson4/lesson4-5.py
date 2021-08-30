# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

from datetime import date
from requests import get, utils
from sys import argv

value = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rates(code_val):
    finder = value.split("<Valute ID=")
    day, month, year = finder[0].split('"')[-4].split(".")

    for n in finder:
        if code_val.upper() in n:
            print(date(year=int(year), month=int(month), day=int(day)), end=": ")
            return float(n.replace("/", "").split("<Value>")[-2].replace(",", "."))

if __name__== "__main__":
    str = argv[1]
    print(currency_rates(str))