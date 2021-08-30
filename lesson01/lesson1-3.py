def procent_write(procent):
    s = procent[-1]
    if s == '1' and procent != '11':
        text = 'процент'
        return text
    elif procent == '11' or procent == '12' or procent == '13' or procent == '14':
        text = 'процентов'
        return text
    elif s == '2' or s == '3' or s == '4':
        text = 'процента'
        return text
    else:
        text = 'процентов'
        return text

procent = input('Введите число процентов: ')

print("Вы ввели: ", procent, "%", procent_write(procent))

