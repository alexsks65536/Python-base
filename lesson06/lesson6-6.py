from sys import argv

with open("trade.csv", "a", encoding="utf-8") as trade_a:
    with open("trade.csv", "r", encoding="utf-8") as trade_r:
        if len(argv) > 1 and [n for n in argv[1:] if n.replace(".", "").isdigit()]:
            if len(argv) == 3:
                print(*trade_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep="\n")
            if "," in argv[1] or "." in argv[1]:
                print(argv[1], file=trade_a)
            else:
                priint(*trade_r.readlines()[int(argv[1]) - 1:], sep="")
        else:
            print(trade_r.read())