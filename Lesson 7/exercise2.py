import enum
from abc import abstractmethod


class Cloth:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def cloth_consumption(self):
        pass

    def get_full_info(self):
        return f'{self.name}. Расход ткани: {self.cloth_consumption}.'


class CoatCloth(Cloth):
    def __init__(self, size):
        self.name = 'Пальто'
        self.size = size

    @property
    def cloth_consumption(self):
        return '%.3f' % (self.size / 6.5 + 0.5)

    def get_full_info(self):
        return f'{super().get_full_info()} Размер: {self.size}'


class CostumeCloth(Cloth):
    def __init__(self, height):
        self.name = 'Костюм'
        self.height = height

    @property
    def cloth_consumption(self):
        return '%.3f' % (self.height * 2 + 0.3)

    def get_full_info(self):
        return f'{super().get_full_info()} Рост: {self.height} см'


class ClothType(enum.Enum):
    id: int
    init: callable(float)

    Coat = (0, CoatCloth)
    Costume = (1, CostumeCloth)

    def __init__(self, id, init):
        self.id = id
        self.init = init


data = [
    (ClothType.Coat, 3000),
    (ClothType.Costume, 180),
    (ClothType.Costume, 140),
    (ClothType.Coat, 4000),
]

clothes = [type.init(param) for type, param in data]

for cloth in clothes:
    print(cloth.get_full_info())
