class Stationery:
    title: str = 'безымянный'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print('Подпись ручкой')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print('Пишем карандашом')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print('Отрисовка маркером')


stationaries = (Stationery(), Pen(), Pencil(), Handle())

for x in stationaries:
    print(f'{x.title}: ', end='')
    x.draw()
