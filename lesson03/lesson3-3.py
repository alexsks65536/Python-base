# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*name):

    str = []
    for i in name:
        for j in name[0]:
            if i[0] == j:
                str.append(i)
    print(str)





thesaurus("Иван", "Мария", "Петр", "Илья", "Маргарита", "Павел", "Дмитрий", "Денис")