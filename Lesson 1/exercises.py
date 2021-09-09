import math
import helpers


def exercise1():
    age = 27
    name = 'Алексей'
    print(f'Привет. Я разработчик {name}. Возраст {age}')

    name = input('Введите свое имя: ')
    result = False
    while not result:
        age_str = input('Введите свой возраст: ')
        result = helpers.is_int(age_str)
    age = int(age_str)
    print(f'Тебя звать {name}. Твой возраст {age}. Через 10 лет тебе будет {age + 10}')


def exercise2():
    full_seconds = helpers.input_by_type('Введите время в секундах и я переведу его в формат чч:мм:сс ', int)
    hh = str(full_seconds // 3600).zfill(2)
    mm = str((full_seconds % 3600) // 60).zfill(2)
    ss = str(full_seconds % 60).zfill(2)
    print(f'{hh}:{mm}:{ss}')


def exercise3():
    value = helpers.input_by_type('Введите неотрицательное число и я проведу вычисления (n + nn + nnn): ', int)
    if value < 0:
        print('Число не может быть отрицательным')
        return
    str_val = str(value)
    new_value = 0
    for i in range(3):
        new_value += int(str_val * (i + 1))
    print(new_value)


def exercise4():
    value = helpers.get_positive_number('Введите целое положительное число и я назову его максимальную цифру: ', int)
    max_int = 0
    i = 0
    while value >= (10 ** i):
        min_v = 10 ** i
        max_v = 10 ** (i + 1)
        cur_val = (value % max_v) // min_v
        max_int = max(max_int, cur_val)
        i += 1
    print(f'Максимальная цифра в числе {value} равна {max_int}')


def exercise5():
    income = helpers.get_positive_number('Введите выручку (приход) фирмы: ', float)
    outcome = helpers.get_positive_number('Введите издержки (расход) фирмы: ', float)
    is_profitable = income > outcome
    cash_message = 'приносит' if is_profitable else 'расходует'

    cash_result_message = f'Фирма {cash_message} деньги.'
    print(cash_result_message)
    if is_profitable:
        print('Рентабельность выручки равна {:.2f}'.format(income / outcome))
        workers_count = helpers.get_positive_number('Введите число сотрудников в фирме: ', int)
        income_by_worker = '{:.2f}'.format(income / workers_count)
        print(f'Прибыль в расчете на сотрудника равна {income_by_worker}')


def exercise6():
    print('Данный скрипт расчитывает через сколько дней вы сможете достигнуть определенного результата тренировок.')
    print('Считаем, что завтра вы пробежите на 10% больше, чем сегодня')
    a = helpers.get_positive_number('Введите сколько километров было пройдено в первый день: ', float)
    b = helpers.get_positive_number('Введите сколько километров вы хотите пробежать: ', float)

    if b < a:
        print('Вы уже достигли желаемого результата')
        return
    k = 1.1  # Модификатор
    approx_day = math.log(b / a, k)
    rounded_day = math.ceil(approx_day)
    print(f'Вы достигнете результата на {rounded_day} день')


if __name__ == '__main__':
    exercise6()
