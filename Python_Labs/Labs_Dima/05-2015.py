from tkinter import *
import random
def clicked_button1():
    Matrix.pop(int(textBox1.get()))
    label2.configure(text=draw_matrix(Matrix))

def fill_matrix(m, n):
    for i in range(m):
        Matrix.append([random.randint(0,9) for i in range(n)])
def draw_matrix(matrix):
    text = " "
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text += str(matrix[i][j]) + " "
        text += "\n"
    return text


m = 5
n = 5
Matrix = []
fill_matrix(m,n)

###
### window
###
window = Tk()
window.title("5-2015-Andreev")
window.geometry("870x250")
###
### label1
###
label1 = Label(window, text="Введите номер строки: ", font=("Arial Bold", 20))
label1.grid(column=0, row=0)
###
### label2
###
label2 = Label(window, text=draw_matrix(Matrix), font=("Arial Bold", 20))
label2.grid(column=0, row=4)
###
###
### textBox1
###
textBox1 = Entry(window,width=46)
textBox1.grid(column=0, row=1)
###
### button1
###
button1 = Button(window, text="Удалить", command=clicked_button1)
button1.grid(column=2, row=0)
###
### end
###
window.mainloop()