def is_int(value):
    try:
        int(value)
        return True
    except:
        return False


def input_by_type(input_text, type):
    if not callable(type):
        raise ValueError('Атрибут type должен быть функцией')
    while True:
        try:
            return type(input(input_text))
        except:
            print(f'Введенное значение не является {type}. Повторите ввод')


def get_positive_number(message, type):
    while True:
        result = input_by_type(message, type)
        if result > 0:
            return result
        else:
            print('Число должно быть больше нуля')


def try_cast(value, type, default_value=None):
    if not callable(type):
        raise ValueError('Атрибут type должен быть функцией')
    try:
        return type(value)
    except:
        return default_value
