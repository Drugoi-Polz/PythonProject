from tkinter import *

def zadanie1(text):
    if len(text) <= 2:
        return False
    for i in range(2, len(text), 2):
        if text[i - 2] != text[i]:
            return False
    return True

def zadanie2(text):
    return text.replace("а", "ак")

def zadanie3(text):
    return text.replace("ку", "")
def clicked_button1():
    if(zadanie1(textBox1.get())):
        label1.configure(text="Верно")
    else:
        label1.configure(text="Неверно")

def clicked_button2():
    label1.configure(text=zadanie2(textBox1.get()))

def clicked_button3():
    label1.configure(text=zadanie3(textBox1.get()))
###
### window
###
window = Tk()
window.title("4-2005-Andreev")
window.geometry("870x250")
###
### label1
###
label1 = Label(window, text="Введите вашу строку: ", font=("Arial Bold", 20))
label1.grid(column=0, row=0)
###
### label2
###
label2 = Label(window, text="Вариант 2\nОпределите, совпадают ли буквы на нечетных местах в слове.\nПосле каждой буквы “а” в слове вставьте букву “к”.\nВычеркните из слова все сочетания “ку”.", font=("Arial Bold", 20))
label2.grid(column=0, row=4)
###
### textBox1
###
textBox1 = Entry(window,width=46)
textBox1.grid(column=0, row=1)
###
### button1
###
button1 = Button(window, text="1 задание", command=clicked_button1)
button1.grid(column=2, row=0)
###
### button2
###
button2 = Button(window, text="2 задание", command=clicked_button2)
button2.grid(column=2, row=1)
###
### button3
###
button3 = Button(window, text="3 задание", command=clicked_button3)
button3.grid(column=2, row=2)
###
### end
###
window.mainloop()