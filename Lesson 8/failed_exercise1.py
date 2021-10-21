# Здесь была попытка сделать проверку по кастомному формату

from enum import Enum
import re


class FormatInfo:
    regex_str = ''  # регулярка для валидации
    groups = {}  # название формата (например yyyy) #: значение

    def append_digit_grp(self, my_str, format_str: str):
        self.groups[format_str] = my_str
        self.regex_str += f'(\\d{{{len(format_str)}}})'


class Date:
    date_str: str

    def __init__(self, date_str: str):
        self.date_str = date_str

    def parse_date_from_str(self, format_string):
        format_info = self.get_format_info(self.date_str, format_string)
        print(format_info.regex_str)
        print(format_info.groups)
        # re.compile(format_info.regex_str)
        print(re.match(format_info.regex_str, self.date_str))
        # values = [e for e in DateTypeEnum]
        # for val in values:

        pass

    @staticmethod
    def get_format_info(date_str: str, format_str: str) -> FormatInfo:
        format_info = FormatInfo()  # format_str
        my_str = ''
        my_format = ''
        format_info.regex_str = '^'
        for i in range(len(date_str)):
            char = date_str[i]
            format_ch = format_str[i]
            if char.isdigit():
                my_str += char
                my_format += format_ch
            else:
                if my_str:
                    format_info.append_digit_grp(my_str, my_format)
                    my_str = ''
                    my_format = ''
                format_info.regex_str += f'\\{char}'
        if my_str:  # записываем последний блок, если он есть
            format_info.append_digit_grp(my_str, my_format)
        format_info.regex_str += '$'
        return format_info


class DateTypeEnum(Enum):
    __id: int
    __format_str: str
    __parser: callable(str)

    Day = (0, 'dd', lambda x: DateTypeEnum.format_int(x, 1, 31))
    Month = (1, 'MM', lambda x: DateTypeEnum.format_int(x, 1, 12))
    Year = (2, 'yyyy', lambda x: DateTypeEnum.format_int(x, 1, 9999))

    def __init__(self, id, format_str, parser):
        self.__id = id
        self.__format_str = format_str
        self.__parser = parser

    @staticmethod
    def format_int(x, min, max):
        if x.isdigit() and min <= x <= max:
            return x
        else:
            raise ValueError


# my_date = Date.parse_date_from_str('dd.MM.yyyy')
my_date = Date('23.04.1994').parse_date_from_str('dd.MM.yyyy')
print(my_date)
