'''
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
'''
import collections
with open("log_file.txt", "w", encoding="utf-8") as log:
    with open("nginx_log.txt", "r", encoding="UTF-8") as log_file:
        research = (f"{s.split()[0]} {s.split()[5][1:]} {s.split()[6]}" for s in log_file)

        for row in research:
            print(row)

with open("log_file.txt", "r", encoding="utf-8") as log:
    new_call = collections.Counter()

    for n in log:
        n = n.split()[0]
        new_call[n] += 1
    spam_ip, counter = new_call.most_common(1)[0][0], new_call.most_common(1)[0][1]
    print(f"Spamer {spam_ip}: {counter} quantity")