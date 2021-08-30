from sys import argv

with open("trade.csv", "r+", encoding="utf-8") as trade_r:
    str, win = argv[1:]
    for s in range(int(str)):
        g = trade_r.tell()
        v = trade_r.readlines().strip()
        if v == "":
            exit('Ошибка: нет такой строки в документе')

    trade_r.seek(g)
    count.write(f"{win + ' ' * (len(n) - len(val))}")