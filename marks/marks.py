import tkinter as tk
import time
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

engine = create_engine("sqlite:////home/fyodor/Documents/Python/Classing_of_marks/users.db", echo=False)

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = 'users'
        
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    sername: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))



welcome = tk.Tk()
welcome.geometry('1920x1080')
welcome.resizable(False, False)
welcome.config(bg='#1e60d4')
welcome.title('Welcome')


#Главная страница

main = tk.Tk()
main.title('Меню')
main.geometry('1920x1080')
main.resizable(False, False)
main.config(bg='#1e60d4')
main.withdraw()

trim_now = 3
trim = tk.Label(main, text=f'Триместр:{trim_now}', font=('Arial', 40)).place(x=0, y=175)

rank = 'B+'
tk.Label(main, text='Учеба', font=('Arial', 40)).place(x=0, y=250)
now_rank_st = tk.Label(main, text=f'Ранг:{rank}', font=('Arial', 40)).place(x=0, y=315)

tk.Label(main, text='Спорт', font=('Arial', 40)).place(x=0, y=390)
now_rank_sp = tk.Label(main, text=f'Ранг:{rank}', font=('Arial', 40)).place(x=0, y=455)

name = tk.Label(main, text='Имя', font=('Arial', 40)).place(x=0, y=10)
sername = tk.Label(main, text='Фамилия', font=('Arial', 40)).place(x=0, y=75)


subjects = ['Выберете предмет','Алгебра', 'Геометрия', 'История']
def select_choose(chooce):
    chooce = variable.get()
    screen_subject=tk.Tk()
    screen_subject.geometry('1920x1080')
    screen_subject.resizable(False, False)
    screen_subject.config(bg='#1e60d4')
    screen_subject.title('Меню предмета')

    tk.Label(screen_subject, font=('Arial', 40), text=chooce,).pack()
    

    screen_subject.mainloop()


# Установка значений для целых чисел
variable = tk.StringVar()
variable.set(subjects[1])

# , command=select_choose

chooce_subject = tk.OptionMenu(main, variable, *subjects)
chooce_subject.config(width=35)
chooce_subject.config(height=5)

chooce_subject.pack()

variable.set(subjects[0])
# chooce_subject.place(x=700, y=50)




def register():
    reg = tk.Tk()
    reg.geometry('1920x1080')
    reg.resizable(False, False)
    reg.config(bg='#1e60d4')
    reg.title('Registration')
    welcome.withdraw()
    n = 1

    name_reg = tk.Entry(reg, font=('Arial', 40), justify='left')
    name_reg.insert(0, 'Имя:')
    name_reg.place(x=500, y=365)

    

    sername_reg = tk.Entry(reg, font=('Arial', 40), justify='left')
    sername_reg.insert(0, 'Фамилия:')
    sername_reg.place(x=500, y=300)

    

    password = tk.Entry(reg, font=('Arial', 40), justify='left', show='*')
    password_txt = tk.Label(reg, text='Пароль:', font=('Arial', 40), bg='white', justify='left').place(x=500, y=430)
    password.place(x=706, y=430)
    psw_first = password.get()

    rep_password = tk.Entry(reg, font=('Arial', 40), justify='left', show='*')
    rep_password_txt = tk.Label(reg, text='Повторите пароль:', font=('Arial', 40), bg='white', justify='left').place(x=500, y=495)
    rep_password.place(x=975, y=495)
    psw_second = rep_password.get()

    def check_password():
        # if password == rep_password and name != '' and sername != '':
            # with Session(engine) as session:
            #     user_1 = User(
            #         id=n,
            #         name = name_reg,
            #         sername = sername_reg,
            #         password = password
            #     )
            # n+=1
            # session.add_all([user_1])
            # session.commit()

            reg.withdraw()
            main.deiconify()
        # else:
        #     warning_psw = tk.Label(reg, text='Ваш пароль не совпал', fg='red', font=('Arial', 40)).place(x=520, y=640)

    check_password = tk.Button(reg, text='Сохранить', font=('Arial', 40), command=check_password)
    check_password.place(x=520, y=560)


    

lable_1 = tk.Label(welcome, text='Добро пожаловать в Classing Marks', font=('Arial', 20)).pack()
register = tk.Button(welcome, text='Регистрация',command=register ,font=('Arial', 40)).place(x=820, y=250)
login = tk.Button(welcome, text='Вход', font=('Arial', 40)).place(x=900, y=350)

welcome.mainloop()


main.mainloop()
