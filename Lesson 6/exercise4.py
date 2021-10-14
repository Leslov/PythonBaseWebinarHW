from random import randint
import time
from abc import ABC

import helpers


class Car:
    speed: float = 0
    color: str = 'красный'
    name: str = 'placeholder name'
    is_police: bool = False
    acceleration: float = 10
    brake_acceleration: float = 40

    def _accelerate(self, goal_speed: float):
        is_increase = self.speed < goal_speed
        if is_increase:
            self.speed = min(self.acceleration + self.speed, goal_speed)
        else:
            self.speed = max(goal_speed, self.speed - self.brake_acceleration)

    def go(self, goal_speed):
        print(f'Целевая скорость: {goal_speed}')
        time.sleep(1)
        while self.speed != goal_speed:
            car._accelerate(goal_speed)
            car.show_speed()
            time.sleep(1)

    def stop(self):
        print('Останавливаем машину')
        time.sleep(1)
        while car.speed != 0:
            car._accelerate(0)
            car.show_speed()
            time.sleep(1)

    def turn(self, direction):
        if direction != 0:
            side = 'вправо' if direction > 0 else 'влево'
            print(f'Поворот на {abs(direction)} градусов {side}')
            time.sleep(1)

    def _get_speed_string(self):
        return f'Текущая скорость = {self.speed} км/ч'

    def show_speed(self):
        print(self._get_speed_string())

    def show_info(self):
        car = f"{('Полицейская машина' if self.is_police else 'Машина')}"
        view_info = f'{self.name}, {self.color} цвет.'
        power_info = f'Разгон в секунду: {self.acceleration} км/ч. Скорость торможения {self.brake_acceleration} км/ч'
        full_info = f'{car} {view_info} {power_info}'
        print(full_info)


class LimitedSpeedCar(Car, ABC):
    _speed_limit: float

    def is_overextending(self):
        return self.speed > self._speed_limit

    def show_speed(self):
        speed_str = Car._get_speed_string(self)
        if self.is_overextending():
            speed_str = f'{speed_str} Превышение скорости!'
        print(speed_str)


class TownCar(LimitedSpeedCar):
    _speed_limit = 60
    name = 'Honda Civic'
    acceleration = 10
    brake_acceleration = 35


class WorkCar(LimitedSpeedCar):
    _speed_limit = 40
    name = 'Волга'
    acceleration = 6
    brake_acceleration = 25


class SportCar(Car):
    name = 'Ferrari 250 GTO'
    acceleration = 25
    brake_acceleration = 49


class PoliceCar(Car):
    is_police = True
    name = 'УАЗ'
    acceleration = 12
    brake_acceleration = 38


def select_car():
    types = ('TownCar', 'SportCar', 'WorkCar', 'PoliceCar')
    for i in range(len(types)):
        print(f'{i + 1}: {types[i]}')
    index = helpers.input_by_type('Укажите номер авто', int, lambda x: 0 < x <= len(types))
    car_type = types[index - 1]
    selected_car = None
    if car_type == 'TownCar':
        selected_car = TownCar()
    elif car_type == 'SportCar':
        selected_car = SportCar()
    elif car_type == 'WorkCar':
        selected_car = WorkCar()
    elif car_type == 'PoliceCar':
        selected_car = PoliceCar()
    else:
        raise ValueError
    return selected_car


car = select_car()
car.show_info()

car.show_speed()
car.go(randint(20, 40))
car.turn(90)
car.go(randint(60, 90))
car.go(randint(15, 25))
car.turn(-90)
car.go(randint(50, 75))
car.stop()
