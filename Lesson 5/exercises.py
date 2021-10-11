import random
import re

import helpers


def exercise1():
    print('Введите строки для записи в файл. Для окончания записи оставьте строку пустой')
    with open('ex1_file.txt', 'w') as file:
        while True:
            string = input()
            if not string:
                break
            file.write(f'{string}\n')


def exercise2():
    with open('ex2_file.txt', encoding='utf8') as file:
        lines = file.readlines()
        print(f'Количество строк в файле: {len(lines)}')
        print('Количество слов по строкам в формате "Num: Count", где Num - номер строки, Count - количество слов')
        words_count = [f'{i + 1}: {len(lines[i].split())} ' for i in range(len(lines))]
        for x in words_count:
            print(x)


def exercise3():
    with open('ex3_file.txt', encoding='utf8') as file:
        employees = {line.split()[0]: float(line.split()[1]) for line in file.readlines()}
        low_money_employees = {surname: money for surname, money in employees.items() if money < 20000}

        if len(low_money_employees) > 0:
            print('Сотрудники с окладом менее 20000: ')
            for surname, money in low_money_employees.items():
                print(surname)
        else:
            print('Нет сотрудников с окладом менее 20000')

        print(f'Средний доход: {helpers.average(employees.values())}')


def exercise4():
    replace_table = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восеь',
        'Nine': 'Девять',
    }
    with open('ex4_input_file.txt', encoding='utf8') as input_file:
        with open('ex4_output_file.txt', 'w', encoding='utf8') as output_file:
            line = input_file.readline()
            while line:
                for eng, rus in replace_table.items():
                    line = line.replace(eng, rus)
                print(line, file=output_file)
                line = input_file.readline()


def exercise5():
    with open('ex5_file.txt', 'w', encoding='utf8') as file:
        numbers = [str(random.randint(1, 100)) for _ in range(random.randint(3, 8))]
        file.write(' '.join(numbers))

    with open('ex5_file.txt', encoding='utf8') as file:
        numbers = [int(num) for num in file.readline().split()]
        print(f'Сумма чисел в файле: {sum(numbers)}')


def exercise6():
    pattern = '(\d*)\((.+?(?=\)))\)' # регулярка для поиска числового значения перед не пустыми скобками
    regular = re.compile(pattern)
    with open('ex6_file.txt', encoding='utf8') as file:
        lines = file.readlines()
        edu_subjects = {}
        for line in lines:
            name = line.split(':', 1)[0]
            lessons = sum([int(x.group(1)) for x in regular.finditer(line)])
            edu_subjects[name] = lessons
        print(edu_subjects)


def exercise7():
    income_list = []
    with open('ex7_input_file.txt', encoding='utf8') as file:
        line = file.readline()
        firms_profit_data = {}
        while line:
            splitted_data = line.split()
            name = splitted_data[0]
            # form = splitted_data[1]
            income = int(splitted_data[2])
            outcome = int(splitted_data[3])
            profit = income - outcome
            firms_profit_data[name] = profit
            line = file.readline()

        avg_profit = helpers.average([x for x in firms_profit_data.values() if x > 0])
        income_list = [firms_profit_data, avg_profit]

    with open('ex7_output_file.txt', 'w', encoding='utf8') as file:
        file.write(str(income_list))
        print(str(income_list))


if __name__ == '__main__':
    exercise7()
