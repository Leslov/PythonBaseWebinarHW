import helpers


def exercise1():
    print('Список элементов и их тип данных: ')
    my_list = ['Alex', 43, False, 'Something', (1, 3, 'HH')]
    for elem in my_list:
        print(f'element - {elem}; type - {type(elem)}')


def exercise2():
    def get_sorted_list(original_list):
        my_bool = False
        new_list = []
        for i in range(len(original_list)):
            elem = original_list[i]
            index = i - my_bool * 1
            new_list.insert(index, elem)
            my_bool = not my_bool
        return new_list
    print('Обмен значений для соседних элементов.')
    my_list = []
    count = helpers.input_by_type('Введите число элементов: ', int)
    for i in range(count):
        my_list.append(helpers.input_by_type(f'Введите элемент №{i + 1}: ', int))
    print(f'Исходный массив:     {my_list}')
    result_list = get_sorted_list(my_list)
    print(f'Обработанный массив: {result_list}')


def exercise3():
    def validate(value):
        if value < 1 or value > 12:
            print('Номер месяца должен быть в пределах от 1 до 12')
            return False
        else:
            return True
    print('К какому сезону относится месяц. ')
    month = helpers.input_by_type('Введите номер месяца: ', int, validate)
    seasons = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
    season = next((key for key, value in seasons.items() if month in value), None)
    print(f'Указанный вами месяц относится к сезону {season}')


def exercise4():
    print('Разделение предложения на слова с ограничением в 10 символов')
    text = input('Введите предложение: ')
    i = 1

    for word in text.split():
        print(word[:10])
        i += 1


def exercise5():
    print('Структура рейтинг и добавление элемента в нее')
    rating = [7, 5, 3, 3, 2]
    int_val = helpers.input_by_type('Введите число для добавления в рейтинг: ', int)
    position = next((i for i in range(len(rating)) if int_val > rating[i]), len(rating))
    print(f'До: {rating}')
    rating.insert(position, int_val)
    print(f'После: {rating}')


def exercise6():

    def parse_prod_string(prod_string, product_format, separator):
        splitted = prod_string.split(separator)
        return {
            product_format[i][0]: product_format[i][1](splitted[i])  # Формат 'ключ : тип(значение)'
            for i in range(len(product_format))
        }

    def get_products(format, separator):
        def is_correct(struct, format, separator):
            if struct == '':
                return True
            result = str(struct).count(separator) == 3
            splitted = struct.split(separator)
            try:
                [format[i][1](splitted[i]) for i in range(len(splitted))]
                result &= True
            except:
                result = False
            if not result:
                print('Введенные данные не соответствуют формату ввода. Повторите попытку')

            return result
        result = []
        i = 1
        while True:
            prod_string = helpers.input_by_type('', str, lambda x: is_correct(x, format, separator))
            if prod_string == '':
                break
            product = parse_prod_string(prod_string, format, separator)
            result.append((i, product))
            i += 1
        return result

    def get_report_string(products, report_formats):
        # здесь был  отчет, как в примере ДЗ
        # report_dict = dict.fromkeys(products[0].keys())
        # for field_key in report_dict.keys():
        #     report_dict[field_key] = [{prod[field_key] for prod in products}]
        # return report_dict
        # return {
        #     key: func([prod[key] for prod in products])  # Формат: 'ключ: функция(список значений)'
        #     for key, func in report_format.items()
        # }
        return {key: func(products) for key, func in report_formats.items()}

    def print_results(products, report):
        print('Получившаяся структура: ')
        for prod in products:
            print(f'\t{prod}')
        print('Отчет: ')
        for report_item in report.items():
            print(f'\t{report_item}')

    def multiply_fields_and_sum(products, i, j):
        return sum([prod[1][i] * prod[1][j] for prod in products])

    print('В этом задании я увлекся чутка, без классов код получился слабочитаемым :)\n')
    print('Структура данных "Товар" и отчет по товарам')
    separator = ';'
    message = 'Введите данные о товаре.\n' \
              'Необходимо указать Название (Н), Розничную Цену (РЦ), Закупочную цену (ЗЦ), Количество (К)\n' \
              f'Формат ввода: "Н{separator}ЗЦ{separator}РЦ{separator}К", без кавычек\n' \
              'Оставьте поле ввода пустым чтобы завершить добавление новых товаров\n'
    print(message)
    fields = ('Название', 'Закупочная цена', 'Розничная цена', 'Количество')
    product_format = (
        (fields[0], str),
        (fields[1], float),
        (fields[2], float),
        (fields[3], float)
    )
    report_format = {
        'Названия': lambda products: ', '.join([prod[1][fields[0]] for prod in products]),
        'Закупочная сумма': lambda products: multiply_fields_and_sum(products, fields[1], fields[3]),
        'Розничная сумма': lambda products: multiply_fields_and_sum(products, fields[2], fields[3]),
        'Ожидаемый доход': lambda products:
        multiply_fields_and_sum(products, fields[2], fields[3]) -
        multiply_fields_and_sum(products, fields[1], fields[3])
    }  # Здесь в лямбде описана функция преобразования данных.

    products = get_products(product_format, separator)
    report = get_report_string(products, report_format)
    print_results(products, report)


if __name__ == '__main__':
    exercise6()
