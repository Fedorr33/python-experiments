import tkinter as tk

main = tk.Tk()
main.title('Меню')
main.geometry('1920x1080')
main.resizable(False, False)
main.config(bg='#1e60d4')


# def checking_mark():
#     mark = mark * 100
#     print(mark)
# new_mark = tk.Entry(main, font=('Arial', 40)).place(x=0, y=150)
# mark = new_mark
trim_now = 3
trim = tk.Label(main, text=f'Триместр:{trim_now}', font=('Arial', 40)).place(x=0, y=175)

rank = 'B+'
tk.Label(main, text='Учеба', font=('Arial', 40)).place(x=0, y=250)
now_rank_st = tk.Label(main, text=f'Ранг:{rank}', font=('Arial', 40)).place(x=0, y=315)

tk.Label(main, text='Спорт', font=('Arial', 40)).place(x=0, y=390)
now_rank_sp = tk.Label(main, text=f'Ранг:{rank}', font=('Arial', 40)).place(x=0, y=455)





name = tk.Label(main, text='Имя', font=('Arial', 40)).place(x=0, y=10)
sername = tk.Label(main, text='Фамилия', font=('Arial', 40)).place(x=0, y=75)


main.mainloop()