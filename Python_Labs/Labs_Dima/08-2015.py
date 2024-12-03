from tkinter import *

def convertTextInList(text):
    textList = []
    text = str(text)
    predlojenie = ""
    i = 0
    while(i < len(text)):
        if (text[i] == "\\" or text[i] == "n"):
            i += 0
        elif(text[i] != "." and text[i] != "!" and text[i] != "?"):
            predlojenie += text[i]
        else:
            textList.append(predlojenie)
            predlojenie = ""
        i += 1
    return textList
def clicked_button1():
    word = textBox1.get()
    textList = convertTextInList(contentFile)
    with open(rexult_path, mode="w", encoding="UTF8") as file:
        for i in textList:
            if word in i:
                file.write(i + "\n")

source_path = "Source.txt"
rexult_path = "Rezult.txt"
rezult_file = open(rexult_path, mode="w", encoding="UTF8")
with open(source_path, mode="r", encoding="UTF8") as file:
    contentFile = file.readlines()

###
### window
###
window = Tk()
window.title("8-2015-Andreev")
window.geometry("870x250")
###
### label1
###
label1 = Label(window, text="Введите ваше слово: ", font=("Arial Bold", 10))
label1.grid(column=0, row=0)
###
### textBox1
###
textBox1 = Entry(window,width=46)
textBox1.grid(column=0, row=1)
###
### button1
###
button1 = Button(window, text="Результат", command=clicked_button1)
button1.grid(column=2, row=0)
###
### end
###
window.mainloop()