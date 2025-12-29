import random

cities = [
    "Архенгельск",
    "Астрахань",
    "Багратионовск",
    "Байкальск",
    "Волгоград",
    "Великий Устюг",
    "Гагарин",
    "Горно-Алтайск",
    "Донецк",
    "Екатеринбург",
    "Енисейск",
    "Железноводск",
    "Жигулевск",
    "Звенигород",
    "Зеленогорск",
    "Иркутск",
    "Ижевск",
    "Йошкар-Ола",
    "Калининград",
    "Казань",
    "Лабинск",
    "Ленинск",
    "Магадан",
    "Магас",
    "Назарово",
    "Назрань",
    "Омск",
    "Обь",
    "Павловск",
    "Певек",
    "Пенза",
    "Ростов Великий",
    "Ростов-на-Дону",
    "Салаир",
    "Самара",
    "Тайга",
    "Талица",
    "Уфа",
    "Ужур",
    "Феодосия",
    "Фокино",
    "Хабаровск",
    "Хвалынск",
    "Цивильск",
    "Циолковский",
    "Чайковский",
    "Чебоксары",
    "Шали",
    "Шатура",
    "Щелкино",
    "Щигры",
    "Электрозаводск",
    "Элиста",
    "Югорск",
    "Югра",
    "Яркутск",
    "Ялта",
]
letter = 1
rend = 1
symvs = 1
symvs_a = 1
answer = 1

cities_used = []


def last_letter_to_answer(word):
    last_letter = word[-1]
    if last_letter == "ь" or last_letter == "ъ" or last_letter == "ы":
        return word[-2]
    else:
        return last_letter


# Функции
def checking(initial_word, answer):
    # Первая проверка (правильное начало слова)
    print(initial_word, answer, last_letter_to_answer(initial_word), answer[0])
    if answer[0] == last_letter_to_answer(initial_word):
        # Вторая проверка (слова не повторяются)
        if answer in cities_used:
            print("Такой город уже был! Так нельзя! Ты плохой человек!")
            return False
        else:
            cities_used.append(answer)
            print(f"Отлично! Принимаю твой ответ {answer}")
            return True

    else:
        # Первая проверка не прошла
        print("Ты жулик! Нужно называть город на последнюю букву!")
        return False

    # symvs_a = list(answer)
    #
    # symvs_a = symvs_a.lower()
    # if symvs_a[0] == symvs[-1]:
    #    return ()
    # else:
    #    return "Это не по правилам! Напиши другой город"


def share(symvs, letter, town):
    symvs = list(town)
    return symvs[-1]


def input_city():
    raw_city_from_user = input()
    city_from_user = raw_city_from_user.lower()
    return city_from_user


def generate_answer(city_from_user):
    letter = last_letter_to_answer(city_from_user)
    filter_list = [
        town for town in cities if letter == town[0] and town not in cities_used
    ]
    if filter_list:
        answer_from_computer = filter_list[0]
        return answer_from_computer
    else:
        # print('-')
        return "-"


# Первый город
rend = random.randint(0, 56)
city_from_computer = cities[rend].lower()
print("Первый город", city_from_computer)

while answer != "-" or answer != "Сдаюсь":
    print("Тебе на", share(symvs, letter, city_from_computer))
    city_from_user = input_city()
    while not checking(city_from_user, city_from_computer):
        city_from_user = input_city()

    city_from_computer = generate_answer(city_from_user)
    if city_from_computer == "-":
        print("Неееет! Я проиграл! Не может быть!")
        break
