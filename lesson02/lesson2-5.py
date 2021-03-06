# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, 45.99, 89.54, 69.25, 36.2, 64, 25.5, 65.97]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
price = [57.8, 46.51, 97, 45.99, 89.54, 69.25, 36.2, 64, 5.5, 65.97, 8.01, 5.70, 99.07, 21.55]

for n in price:
    rubles, coins = str(f"{n :.2f}").split(".")
    print(f"{rubles} руб {int(coins):02} коп, ", end=" ")

print(f"ID one: {id(price)} - {price}")
price.sort()
print(f"ID two: {id(price)} - {price}")

""" Variant с & d"""

print(f"ID one: {id(sorted(price))} - {sorted(price, reverse=True)}\n{sorted(price)[-5:]}")