import math

import helpers
import random
from functools import reduce
from itertools import cycle


def exercise1():
    def calculate_salary(hours, rate, bonus):
        return hours * rate + bonus

    print('Расчет зп сотрудника по формуле час * ставка + премия')
    hours = helpers.input_by_type('Введите кол-во часов', float)
    rate = helpers.input_by_type('Введите ставку', float)
    bonus = helpers.input_by_type('Введите размер премии', float)
    salary = calculate_salary(hours, rate, bonus)
    print(f'Заработная плата составляет {salary}')


def exercise2():
    numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    new_numbers = [numbers[i] for i in range(len(numbers)) if (i > 0 and (numbers[i] > numbers[i - 1]))]
    print(f'Исходный список:   {numbers}')
    print(f'Полученный список: {new_numbers}')


def exercise3():
    print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])


def exercise4():
    mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    newlist = [x for x in mylist if mylist.count(x) == 1]
    print(f'Исходный список:   {mylist}')
    print(f'Полученный список: {newlist}')


def exercise5():
    mylist = [x for x in range(100, 1001, 2)]
    print('Получаем результат умножения всех четных элементов списка от 100 по 1000')
    print(reduce((lambda x, y: x * y), mylist))


def exercise6():
    def get_numbers(start):
        foo = math.floor(math.log10(start)) + 1  # число десятков
        end = int(math.pow(10, foo))
        return [x for x in range(start, end)]

    def cycle_some():
        i = 0
        mylist = []
        for x in cycle([1, 2, 3, 4, 5]):
            if i >= 11:
                break
            i += 1
            mylist.append(x)
        return mylist

    start = helpers.input_by_type('Введите стартовое число', int)
    print(get_numbers(start))
    print('А теперь - цикл через cycle()')
    print(cycle_some())


def exercise7():
    def fact(x):
        res = 1
        for i in range(1, x + 1):
            res = res * i
            yield res

    n = helpers.input_by_type('Введите число, для которого найдем факториал', int)
    for el in fact(n):
        print(el)


if __name__ == '__main__':
    exercise7()
