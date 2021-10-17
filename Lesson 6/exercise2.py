class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_required_asphalt_mass(self, asphalt_unit_mass: int, thickness: int):
        return self.get_size() * asphalt_unit_mass * thickness

    def get_size(self):
        return self._length * self._width


width = 20
length = 4500
thickness = 4
asphalt_unit_mass = 22

my_road = Road(length, width)
print(f'Вес единицы асфальта - {asphalt_unit_mass}кг (для покрытия площади 1 кв.м. толщиной 1см)')
print(f'Расчет массы асфальта для покрытия дороги площадью {my_road.get_size()} кв.м. ({length}м x {width}м)')
total_mass_ton = int(my_road.calculate_required_asphalt_mass(asphalt_unit_mass, thickness) / 1000)
print(f'Необходимая масса для покрытия дороги толщиной {thickness}см - {total_mass_ton}т')
