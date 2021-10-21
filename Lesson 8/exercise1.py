import datetime
import enum





class Date:
    date_str: str
    __months = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря'
    }
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def parse_date(cls, date_str):
        self = cls(date_str)
        try:
            year, month, day = [int(x) for x in self.date_str.split('-')]
        except:
            return 'Не удалось распознать дату'
        if Date.validate(year, month, day):
            return f'{day} {self.__months[month]} {year}г.'
        else:
            return 'Введенная дата не является корректной'

    @staticmethod
    def validate(year, month, day):
        return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999

today = str(datetime.date.today())
print(f'Текущая дата: {Date.parse_date(today)}')
print(Date.parse_date('something really wrong'))
print(Date.parse_date('1994-04-23'))
print(Date.parse_date('0000-00-00'))
print(Date.parse_date('0001-01-01'))
print(Date.parse_date('1990-13-01'))
