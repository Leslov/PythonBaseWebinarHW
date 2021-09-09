import exercises

# здесь будет форма выбора
import helpers

exercises_list = (
    exercises.exercise1,
    exercises.exercise2,
    exercises.exercise3,
    exercises.exercise4,
    exercises.exercise5,
    exercises.exercise6
)
end = False
while not end:
    msg = 'Введите номер упражнения для проверки. От 1 до 6. Или любую клавишу для завершения: '
    exc = input(msg)
    exc_num = helpers.try_cast(exc, int, -1)

    if exc_num <= 0 or exc_num > 6:
        break
    print('\n****************\n')
    print(f'Упражнение №{exc_num}')
    exercises_list[exc_num - 1]()
    print('\n****************\n')
