try:
    duration = int(input("Введите интервал в секундах: "))
except ValueError:
    print("Нужно ввести число секунд!")
else:

    minuts = duration // 60
    hours = minuts // 60
    days = hours // 24
    years = days // 365

    if duration < 60:
        print("Период: ", duration, "сек")
    elif duration < 60*60:
        print("Период: ", minuts, "мин", duration % 60, "сек")
    elif duration < 60*60*24:
        print("Период: ", hours, "час", minuts % 60, "мин", duration % 60, "сек")
    elif duration < 60*60*24*365:
        print("Период: ", days, "сут", hours % 24, "час", minuts % 60, "мин", duration % 60, "сек")
    else:
        print("Период: ", years, "лет", days % 365, "сут", hours % 24, "час", minuts % 60, "мин", duration % 60, "сек")

# import hello_module

# hello_module.say_hello('Лена')
