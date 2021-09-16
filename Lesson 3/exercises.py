import helpers


def exercise1():
    def div_with_zero_check(divisible, divisor):
        if not divisor:
            print('Попытка деления на ноль!')
        else:
            return div(divisible, divisor)

    def div(divisible, divisor):
        return divisible / divisor

    print('Делим одно число на другое, используя функцию, с учетом попытки деления на ноль')
    num1 = helpers.input_by_type('Введите делимое', float)
    num2 = helpers.input_by_type('Введите делитель', float)

    msg = 'Вариант №1: обработка деления на ноль внутри функции. ' \
          'Минусы - такая реализация вынуждает знать внутренности функции'
    print(msg)
    result = div_with_zero_check(num1, num2)
    if result is not None:
        print(result)

    msg ='Вариант №2: Обработка деления на ноль вне функции. ' \
          'Можно не знать внутренностей функции, но нужно обработать снаружи'
    print(msg)
    if not num2:
        print('Попытка деления на ноль!')
    else:
        print(div(num1, num2))

def exercise2():
    def format_user_data(name, surname, year, city, email, phone):
        return f'{surname} {name}, {year} года рождения, проживает в {city}. \n' \
               f'Контактные данные: телефон - {phone}, email - {email}'

    data = format_user_data('Алексей', 'Павлов', 1994, 'п. Приютово', 'my_mail@example.com', 88005553535)
    print(data)


def exercise3():
    def my_func(arg1, arg2, arg3):
        return sorted([arg1, arg2, arg3])[-2:]

    my_values = [11, 2, 4]
    print('Топ 2 элемента из 3')
    print(f'Было: {my_values}')
    print(f'Результат: {my_func(*my_values)}')


def exercise4():
    def my_pow(x: float, y: int):  # Функция работает не только для отрицательных степеней
        result = 1.0
        for i in range(abs(y)):
            result *= x if y >= 0 else 1 / x
        return result

    print('Возводим число в степень без встроенных функций')
    x = helpers.input_by_type('Введите действительное положительное число', float, lambda num: num > 0)
    y = helpers.input_by_type('Введите целое отрицательное число', int, lambda num: num < 0)
    z = my_pow(x, int(y))
    print(f'my_pow({x}, {y}) = {my_pow(x, y)}')
    print(f'      {x} ** {y} = {x ** y}')


def exercise5():
    end_symbol = ';'

    def decode(input_raw: str):
        nonlocal end_symbol
        has_end_symbol = end_symbol in input_raw
        if has_end_symbol:
            input_raw = input_raw.split(end_symbol, 1)[0].strip() + ' 0'  # Костыль, чтобы условия не плодить
        values = input_raw.strip().split()
        if not all(x.lstrip('-').replace('.', '').isdecimal() for x in values):  # Громоздкая проверка получилась :/
            print('Некорректный ввод')
            return (), False
        else:
            return (float(x) for x in values), has_end_symbol

    print('Скрипт принимает на вход строку чисел, разделенные пробелами и суммирует их')
    print(f'Введите строку чисел разделенных пробелом.\nДля завершения ввода используется символ {end_symbol}')
    result_summ = 0.0
    has_end_symbol = False
    while not has_end_symbol:
        input_raw = input()
        numbers, has_end_symbol = decode(input_raw)
        result_summ += sum(numbers)
        print(f'Текущая сумма = {result_summ}')
    print('Успехов вам!')


def exercise6():
    def int_func(latin_word: str):
        return latin_word.capitalize()

    print(int_func(input('Введите слово и я сделаю первую букву большой.')))


def exercise7():
    def int_func(latin_word: str):
        return latin_word.capitalize()

    input_raw = input('Введите предложение и я сделаю первую букву каждого слова большой.')
    result = ' '.join(int_func(x) for x in input_raw.strip().split())
    print(result)


if __name__ == '__main__':
    exercise1()
