from tkinter import *
import random
def clicked_button1():
    Matrix.pop(int(textBox3.get()))
    label4.configure(text=draw_matrix(Matrix))
def clicked_button2():
    fill_matrix(int(textBox1.get()), int(textBox2.get()))
    label4.configure(text=draw_matrix(Matrix))

def fill_matrix(m, n):
    Matrix.clear()
    for i in range(m):
        Matrix.append([random.randint(0,9) for i in range(n)])
def draw_matrix(matrix):
    text = " "
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text += str(matrix[i][j]) + " "
        text += "\n"
    return text

Matrix = []

###
### window
###
window = Tk()
window.title("5-2015-Julie")
window.geometry("420x400")
###
### label1
###
label1 = Label(window, text="Введите количество строк: ", font=("Arial Bold", 20))
label1.grid(column=0, row=0)
###
### label2
###
label2 = Label(window, text="Введите количество столбцов: ", font=("Arial Bold", 20))
label2.grid(column=0, row=2)
###
### label3
###
label2 = Label(window, text="Введите номер строки: ", font=("Arial Bold", 20))
label2.grid(column=0, row=5)
###
### label4
###
label4 = Label(window, text=draw_matrix(Matrix), font=("Arial Bold", 20))
label4.grid(column=0, row=8)
###
### textBox1
###
textBox1 = Entry(window,width=46)
textBox1.grid(column=0, row=1)
###
### textBox2
###
textBox2 = Entry(window,width=46)
textBox2.grid(column=0, row=3)
###
### textBox3
###
textBox3 = Entry(window,width=46)
textBox3.grid(column=0, row=6)
###
### button1
###
button1 = Button(window, text="Удалить", command=clicked_button1)
button1.grid(column=0, row=7)
###
### button2
###
button1 = Button(window, text="Сгенерировать", command=clicked_button2)
button1.grid(column=0, row=4)
###
### end
###
window.mainloop()