import curses



def main(screen):
    # Настраиваем цвета
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Очистка Экрана
    screen.clear()

    # Текст
    print('Привет это моя игра Minecraft, давай поиграем')

    #Координаты игрока(начальные)
    x, y = 5, 10
    hight_land = 18

    #Размер поля
    long, hight = 40, 30

    # Выводим цветные символы в разные позиции
    #screen.addch(строка, столбец, символ, атрибуты)
    screen.addch(5, 10, '@', curses.color_pair(1))   # Красный игрок
    screen.addch(5, 12, '#', curses.color_pair(2))   # Зелёный блок
    screen.addch(6, 11, '~', curses.color_pair(3))   # Синяя вода
    screen.addch(7, 10, '*', curses.color_pair(4))   # Жёлтый к
    # Создание мира
    hight == 30
    long == 40
    for i in range(39):
        stdscr.addch(i, 0, '|')
        stdscr.addch(i, 39, '|')
        stdscr.addch(39, i, '|')
        stdscr.addch(0, i, '|')
        stdscr.addch(i, 20, '#', curses.color_pair(2))
        stdscr.addch(i, 19, '#', curses.color_pair(2))
        stdscr.addch(i, 18, '#', curses.color_pair(2))
        stdscr.addch(i, hight_land-1, '*', curses.color_pair(4))

    #Ожидание клавиши
    screen.getch()
    #Получаем ввод пользователя
    key = screen.getch()

    # Обработка ввода пользователя
    if key == org('s') and y>1:
        y -= 1
    elif key == ord('w') and y>1:
        y += 1
    elif key == ord('a') and x>1:
        x -= 1
    elif key == ord('d') and x<1:
        x += 1

    # Обновляем позицию игрока на экране
    screen.addch(y, x, '@', curses.color_pair(1))

curses.wrapper(main)
