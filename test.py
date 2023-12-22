from tkinter import *
from tkinter.ttk import Combobox

def btn_click():
    mark = 0
    
    # №1 
    entered_answer = entry_answer.get().lower()
    correct_answer = "="
    if entered_answer.strip() == correct_answer: 
        mark += 2

    # №2
    if v1.get() == 2:
        mark += 2

    # №3
    selected_answer = combo.get()
    correct_answer = "H24"
    if selected_answer == correct_answer:
        mark += 2
        
    # №4
    if scale_var.get() == 1:
        mark += 2
        
    # №5
    if v2.get() == 2:
        mark += 2
        
    # №6
    if v3.get() == 0 and v4.get() == 0 and v5.get() == 1 and v6.get() == 1:
        mark += 2
    elif v3.get() == 0 and v4.get() == 0 and v5.get() == 1 and v6.get() == 0:
        mark += 1
    elif v3.get() == 0 and v4.get() == 0 and v5.get() == 0 and v6.get() == 1:
        mark += 1
    

    # Відповідь
    if mark > 6:
        lbl12["fg"] = "green"  
    else:
        lbl12["fg"] = "red"  
    v7.set("Ваша оцінка: " + str(mark))

tk = Tk()
tk.config (cursor="cross", highlightcolor='#006400', highlightthickness=4)
tk.title("Електронні таблиці Excel")
font_title = ("Georgia", 14, "bold")
font_q = ("Georgia", 12, "bold")

# №1
lbl1 = Label(tk, text="Питання №1", font=font_title)
lbl1_1 = Label(tk, text="Яким оператором починається функція в Excel?", font=font_q)
entry_answer = Entry(tk)
lbl1.pack()
lbl1_1.pack()
entry_answer.pack()

# №2
lbl2 = Label(tk, text="Питання №2", font=font_title)
lbl3 = Label(tk, text=" Яка з формул записана НЕ правильно?", font=font_q)
v1 = IntVar()

rbt1 = Radiobutton(tk, text="=А5*А6", variable=v1, value=1)
rbt2 = Radiobutton(tk, text="В3+А9=48", variable=v1, value=2)
rbt3 = Radiobutton(tk, text="=А4/В7", variable=v1, value=3)
rbt4 = Radiobutton(tk, text="=100-А1", variable=v1, value=4)
lbl2.pack()
lbl3.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()

# №3 
lbl6 = Label(tk, text="Питання №3", font=font_title)
lbl7 = Label(tk, text="Якщо номер рядка 24, а номер стовпця Н , то адреса комірки буде:", font=font_q)
answers = ("H24","24Н","2Н4","Н2.4")
combo = Combobox(tk, values=answers)
lbl6.pack()
lbl7.pack()
combo.pack()

# №4
lbl8 = Label(tk, text="Питання №4", font=font_title)
lbl8_1 = Label(tk, text="З якої цифри починається нумерація рядків в таблиці Excel:", font=font_q)
scale_var = IntVar()
scale = Scale(tk, from_=0, to=1, orient=HORIZONTAL, variable=scale_var)
lbl8.pack()
lbl8_1.pack()
scale.pack()

# №5
lbl9 = Label(tk, text="Питання №5", font=font_title)
lbl10 = Label(tk, text="Яке основне призначення електронних таблиць?*", font=font_q)
v2 = IntVar()
rb1 = Radiobutton(tk, text="Рядком", variable=v2, value=1)
rb2 = Radiobutton(tk, text="Листом", variable=v2, value=2)
rb3 = Radiobutton(tk, text="Книгою", variable=v2, value=3)
rb4 = Radiobutton(tk, text="Коміркою", variable=v2, value=4)
lbl9.pack()
lbl10.pack()
rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()

# №6
lbl11 = Label(tk, text="Питання №6", font=font_title)
lbl12 = Label(tk, text="Документ, створений в табличному процесорі називають:", font=font_q)
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
chb1 = Checkbutton(tk, text="Подання числової інформації в графічному вигляді", variable=v3, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Введення текстової інформації та її опрацювання", variable=v4, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Опрацювання числових даних та автоматизація обчислень", variable=v5, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Створення таблиць", variable=v6, onvalue=1, offvalue=0)
lbl11.pack()
lbl12.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()

btn = Button(tk, text="Відповісти", command=btn_click)

v7 = StringVar()
lbl12 = Label(tk, text='', textvariable=v7)

btn.pack()
lbl12.pack()

tk.mainloop()
