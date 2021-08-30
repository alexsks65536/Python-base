from functools import wraps

def type_logger(func):

    @wraps(func)   #сокрытие функции декоратора
    def wrapper(*args, **kwargs):
        row = [i for i in (*args, *kwargs.values())]
        s = [f"{func.__name__}({i}: {type(i)})" for i in row]
        print(*s, *func(*args, **kwargs), sep=",\n")

    return wrapper

@type_logger
def calc_cube(*x, **y):
    row = [i for i in (*x, *y.values()) if isinstance(i, int) or isinstance(i, float) or isinstance(i, complex)]
    d = [m ** 3 for m in row]
    return d

any = calc_cube(1, [2, 3], 4, {5: 6}, 7, 8.56, {9, 10}, ('val', 19), {'name': 17}, 'abcd', name_is='John')
help(calc_cube)
print(calc_cube.__name__)