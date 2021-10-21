#  Описание задания плохо понятно.
class IsDigitOnly(Exception):
    text = 'В списке присутствуют не только числа'
    @classmethod
    def validate(cls, list):
        for x in list:
            try:
                int(x)
            except:
                raise cls

my_list = []
print('Введите числа разделенные пробелом. Введите stop для завершения ввода')
while (True):
    try:
        input_str = input()
        if input_str == 'stop':
            print(my_list)
            exit()
        data = input_str.split()
        IsDigitOnly.validate(data)
        for x in data:
            my_list.append(int(x))
    except IsDigitOnly as e:
        print(e.text)
