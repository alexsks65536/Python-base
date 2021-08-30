# Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы.

dictionary = {
              'zero': 'ноль',
              'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'
            }

def num_translate(num):
    num_low = num.lower()
    for key, value in dictionary.items():
        if key == num_low:
            if num[0].isupper():
                return value.capitalize()
            return value

print(num_translate(input("Введите число: ")))
