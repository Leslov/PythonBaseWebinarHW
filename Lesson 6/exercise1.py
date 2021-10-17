from time import sleep


class TrafficLight:
    class Color:
        name: str
        delay: int

        def __init__(self, name, delay):
            self.name = name
            self.delay = delay

    __color: str
    __color_variants = (Color("Red", 7), Color("Yellow", 2),Color("Green", 8))

    def running(self):
        for color in self.__color_variants:

            self.__color = color.name
            print(f'Текущий цвет: {self.__color}')
            sleep(color.delay)
        self.__color = None


traf = TrafficLight()
traf.running()
