# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for index, value in enumerate(my_list):
    if value.replace("+", "").replace("-", "").isdigit():
        if value.isdigit():
            my_list[index] = f"{int(value):02}"
        else:
            my_list[index] = f"{value[0]}{int(value[1:]):02}"

print(my_list)
print(" ".join(my_list))