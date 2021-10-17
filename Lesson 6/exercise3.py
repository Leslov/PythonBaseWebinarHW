class Worker:
    name: str
    surname: str
    position: str

    def _get_income(self, hours: float):
        income_info = self.__income_details[self.position]
        return income_info["rate"] * hours + income_info["bonus"]

    __income_details = {
        'Junior': {"rate": 200, "bonus": 4000},
        'Middle': {"rate": 400, "bonus": 6000},
        'Senior': {"rate": 600, "bonus": 8000},
    }


class Position(Worker):
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income_by_hours(self, hours):
        return self._get_income(hours)


hours = 200
junior_position = Position('Василий', 'Петров', 'Junior')
total_income = junior_position.get_total_income_by_hours(hours)

print(f'Сотрудник {junior_position.get_full_name()}. Должность {junior_position.position}.')
print(f'Заработная плата при отработанных {hours} часах равняется {total_income} руб.')
