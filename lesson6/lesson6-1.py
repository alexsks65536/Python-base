'''
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
value = utils.get_unicode_from_response(get(" "))
'''
with open("nginx_log.txt", "r", encoding="UTF-8") as log_file:
    research = ((s.split()[0], s.split()[5][1:], s.split()[6]) for s in log_file)
    i = 0
    for row in research:
        print(row)
        i += 1
    print(f"Количество строк: {i}")

'''
Второй вариант первой задачи
'''
with open("log_file.txt", "w", encoding="utf-8") as log:
    with open("nginx_log.txt", "r", encoding="UTF-8") as log_file:
        research = (f"{s.split()[0]} {s.split()[5][1:]} {s.split()[6]}" for s in log_file)
        i = 0
        for row in research:
            print(row)
            i += 1
        print(f"Количество строк: {i}")


