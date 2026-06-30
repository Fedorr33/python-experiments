import curses

def main(screen):
    # Настраиваем цвета
    curses.start_color()
    
    # Выводим цветные символы в разные позиции
    # screen.addch(строка, столбец, символ, атрибуты)
    screen.addch(5, 10, '@', curses.color_pair(1) | curses.A_BOLD)   # Красный игрок
    screen.addch(5, 12, '#', curses.color_pair(2))                    # Зелёный блок
    screen.addch(6, 11, '~', curses.color_pair(3) | curses.A_BOLD)   # Синяя вода
    screen.addch(7, 10, '*', curses.color_pair(4))                    # Жёлтый камень
    
    # Выводим текст
    screen.addstr(10, 5, "Это основа для твоей игры!")
    screen.addstr(11, 5, "Нажми любую клавишу для выхода...")
    
    # Показываем всё на экране
    screen.refresh()
    
    # Ждём нажатия любой клавиши
    screen.getch()

# Запускаем программу
if __name__ == "__main__":
    curses.wrapper(main)
