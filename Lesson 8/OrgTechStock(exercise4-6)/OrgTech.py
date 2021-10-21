class OrgTech:
    name: str

    def __str__(self):
        return self.name


class Scaner(OrgTech):
    name = 'Сканер'

    def __str__(self):
        return self.name

    def get_scan(self):
        return 'Содержимое отсканированного документа'


class Printer(OrgTech):
    name = 'Принтер'

    def print(self, doc):
        pass


class Xerox(OrgTech):
    name = 'Ксерокс'

    def get_copy(self):
        #  Тут происходит процесс копирования
        pass

    def scan(self):
        return 'Отсканированный документ'

    def print(self, doc):
        #  Тут вызываем печать
        pass
