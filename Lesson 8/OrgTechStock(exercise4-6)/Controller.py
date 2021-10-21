import helpers
from OrgTechContainer import Department, Stock
from OrgTech import OrgTech, Scaner, Xerox, Printer


def init_orgtech_list(orgtech_class, count):
    return [orgtech_class() for i in range(count)]


stock = Stock()
programmer_dep = Department('Отдел программистов')
consult_dep = Department('Отдел техподдержки')
departments = [programmer_dep, consult_dep]

scaners = init_orgtech_list(Scaner, helpers.input_by_type('Введите сколько пришло сканеров на склад: ', int))
printers = init_orgtech_list(Printer, helpers.input_by_type('Введите сколько пришло принтеров на склад: ', int))
xeroxs = init_orgtech_list(Xerox, helpers.input_by_type('Введите сколько пришло ксероксов на склад: ', int))

stock.import_orgtech(*scaners)
stock.import_orgtech(*printers)
stock.import_orgtech(*xeroxs)

if input('Желаете распределить оргтехнику по отделам? y - да, иначе - нет: ') == 'y':
    print('Выберите отдел:')
    print("\n".join([f"{i + 1}: {departments[i]}" for i in range(len(departments))]))
    index = helpers.input_by_type('', int, lambda x: 1 <= x <= len(departments))
    destination = departments[index - 1]

    types = [Scaner, Printer, Xerox]
    print('Выберите тип техники: 1: сканер, 2: принтер, 3: ксерокс')
    index = helpers.input_by_type('', int, lambda x: 1 <= x <= 3)
    type = types[index - 1]

    count = helpers.input_by_type('Введите количество: ', int)

    stock.export_orgtech_by_type(destination, type, count)
    destination.print_info()
