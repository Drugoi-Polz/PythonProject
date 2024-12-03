from tkinter import *

def zadanie1(text):
    text = text.lower()
    rezult = ""
    for i in range(len(text)):
        if not(text[i] in rezult):
            rezult += text[i]
    return len(rezult)
def zadanie2(text):
    text = text.lower()
    rezult = ""
    glasnie = "аеёуыяиоюэ"
    for i in range(len(text)):
        if not(text[i] in glasnie):
            rezult += text[i]
    return rezult

def zadanie3(text):
    rezult = ""
    for i in range(len(text) - 1, -1, -1):
        rezult += text[i]
    return rezult
def clicked_button1():
    label1.configure(text=zadanie1(textBox1.get()))

def clicked_button2():
    label1.configure(text=zadanie2(textBox1.get()))

def clicked_button3():
    label1.configure(text=zadanie3(textBox1.get()))
###
### window
###
window = Tk()
window.title("4-2005-Julie")
window.geometry("360x100")
###
### label1
###
label1 = Label(window, text="Введите вашу строку: ", font=("Arial Bold", 20))
label1.grid(column=0, row=0)
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