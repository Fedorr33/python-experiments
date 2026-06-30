import time
import random

time_limit = 5


level = int(input('Введите уровень сложности 1-5 '))
def math(level, value_1, value_2, time_limit):
    if level == 1:
        value_1 = random.randint(0, 9)
        value_2 = random.randint(0, 9)
        return value_1
        return value_2
        example = value_1 * value_2

        start_time = time.time()
        answer = int(input(f'{value_1}, *, {value_2}, = '))
        end_time = time.time()
        time_dif = end_time - start_time

        if time_dif >= 5:
            print('Ты не успел')
            if answer == example:
                print('Верно молодец')
            else:
                print('Твой ответ неверный')
        else:
            print('Ты не успел')
math(level, value_1, value_2, time_limit)
