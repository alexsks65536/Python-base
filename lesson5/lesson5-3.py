'''
    Есть два списка.
    Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
    ('Иван', '9А')
    ('Анастасия', '7В')
'''
from itertools import islice, zip_longest

tutors = [
     'Иван', 'Анастасия', 'Петр', 'Сергей',
     'Дмитрий', 'Борис', 'Елена'
 ]
klasses = [
     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
 ]
print('*' * 18, 'Первый вариант', '*' * 18)

row = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(*row, sep='\n')

print('*' * 18, 'Второй вариант', '*' * 18)

sequence = (n for n in zip_longest(tutors, klasses))
print(*islice(sequence, 9), sep="\n")




