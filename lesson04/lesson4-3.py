# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату
# из ответа, какой тип данных лучше использовать в ответе функции?

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

print(currency_rates("USd"))
print(currency_rates("euR"))