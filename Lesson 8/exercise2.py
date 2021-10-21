import helpers


class MyZeroDivisionError(Exception):
    def __init__(self, text='Попытка деления на ноль!'):
        self.text = text


def div(x, y):
    if y == 0:
        raise MyZeroDivisionError
    else:
        return x / y


x = helpers.input_by_type('Введите делимое', int)
y = helpers.input_by_type('Введите делитель', int)
try:
    print(f'{x}/{y} = {div(x, y)}')
except MyZeroDivisionError as e:
    print(e.text)
