from abc import ABC
import OrgTech


class OrgTechContainer:  # Абстрактный класс, описывающий способность импорта, хранения и экспорта оргтехники
    _orgtech_list: list
    name: str

    def __init__(self):
        self._orgtech_list = []

    def __str__(self):
        return self.name

    def import_orgtech(self, *args: OrgTech):
        for arg in args:
            self._orgtech_list.append(arg)

    def export_orgtech_by_type(self, destination, orgtech_type, count):
        export_list = []
        remains_count = count
        for i in range(len(self._orgtech_list)):
            if remains_count <= 0:
                break
            if type(self._orgtech_list[i]) == orgtech_type:
                remains_count -= 1
                export_list.append(self._orgtech_list[i])

        for arg in export_list:
            self._orgtech_list.remove(arg)
            destination.import_orgtech(arg)

        print(f'{orgtech_type.__name__} в количестве {count - remains_count} успешно отправлен в {destination}')

    def print_info(self):
        print('****************************')
        mylist = '\n'.join([str(x) for x in self._orgtech_list])
        print(f'Состав оргтехники в {self.name}:\n{mylist}')
        print('****************************')


class Stock(OrgTechContainer):
    def __init__(self):
        super().__init__()


class Department(OrgTechContainer):

    def __init__(self, name: str):
        super().__init__()
        self.name = name
