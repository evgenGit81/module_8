# -*- coding: utf-8 -*-

def add_everything_up(a, b):
    """Функция суммирования всего"""
    try:
        c = a + b
        return c
    except TypeError:
        print("Несовпадение форматов, но я сcуммирую:")
        bb = str(b)
        aa = str(a)
        c = aa + bb
        return c


print(add_everything_up(2, 8))
print(add_everything_up(2, 123.765))
print(add_everything_up(2, "4hzdfhzf"))
print(add_everything_up("kg2", "4hzdfhzf"))
print(add_everything_up("kg2", 67.98))
