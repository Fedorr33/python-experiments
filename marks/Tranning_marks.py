# from typing import List
# from typing import Optional
# from sqlalchemy import ForeignKey
# from sqlalchemy import String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from sqlalchemy import select
 

# engine = create_engine("sqlite:////home/fyodor/Documents/Python/Classing_of_marks/marks.db", echo=False)

# class Base(DeclarativeBase):
#     pass
# class Mark(Base):
#     __tablename__ = 'marks'
    
#     id: Mapped[int] = mapped_column(primary_key=True)
#     subject: Mapped[str] = mapped_column(String(30))
#     mark: Mapped[int] = mapped_column()

# def insert_data():
#     History = marks()

# with Session(engine) as session:
#     mark_1 = Mark(
#         subject='История',
#         mark = 5,
#         id = 4
#     )
#     session.add_all([mark_1])
#     session.commit()


#Вывод таблицы
# session = Session(engine)
# stmt = select(Mark).where(Mark.subject.in_(["История", "Алгебра"]))
# #results = session.execute(stmt).all()

# marks = session.scalars(stmt)
# for mark in marks:
#     print(mark.id, " ", mark.subject, " ", mark.mark)
# for Mark in session.scalars(stmt):
#     print(marks)from tkinter import *

import tkinter as tk
ws = tk.Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B90C')

def display_selected(choice):
    choice = variable.get()
    print(choice)

countries = ['Bahamas','Canada', 'Cuba','United States']

# setting variable for Integers
variable = tk.StringVar()
variable.set(countries[3])

# creating widget
dropdown = tk.OptionMenu(
    ws,
    variable,
    *countries,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)



# subjects = ['Выберете предмет','Алгебра', 'Геометрия', 'История']
# def select_choose(chooce):
#     chooce = variable.get()
#     print(variable)
# # Установка значений для целых чисел
# variable = tk.StringVar()
# variable.set(subjects[1])

# chooce_subject = tk.OptionMenu(main, variable, *subjects, command=select_choose)
# chooce_subject.config(width=35)
# chooce_subject.config(height=5)
# chooce_subject.pack()
# infinite loop 
ws.mainloop()



