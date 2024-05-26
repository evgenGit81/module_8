# -*- coding: utf-8 -*-
class MyException(Exception):
    """Вводит сообщение об ошибке"""
    def __init__(self, value):
        self.msg = value
    def __str__(self):
        return self.msg


def func_append(dict_a, b, c):
    """Добавляет в словарь и ечатает словарь """
    if b.isalpha() == False:
        raise MyException("InvalidDataException")
    elif c.isdigit() == False:
        raise MyException("InvalidDataException")
    else:
        dict_a[b] = c
        print(dict_a)


def func_cub(n):
    """Возводит число в степень числа"""
    if n.isnumeric() == False:
        raise MyException("ConditionError")
    else:
        return int(n) ** int(n)

dict_a = dict()
for i in range(2):
    b = input("Введите ключ (должны быть только буквы): ")
    try:
        result = func_append(dict_a, b, input("Введите значение ключа (должны быть только цифры): "))
    except MyException as ee:
        print(f"{ee}: Введены неправильные данные!")

n = input("Введите целое число: ")
try:
    result2 = func_cub(n)
    print("Вы ввели число: ", n, "Ваш результат: ", result2)
except MyException as ee:
    print(f"{ee}: Ошибка! Нарушение условия ввода!")