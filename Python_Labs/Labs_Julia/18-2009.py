class Student:

    def __init__(self, familiya=None, imya=None, otchestvo=None, data=None, nomerZachetki=None, text=None):
        if text is None:
            self.familiya = familiya
            self.imya = imya
            self.otchestvo = otchestvo
            self.data = data
            self.nomerZachetki = nomerZachetki
        else:
            text = text.split()
            self.familiya = text[0]
            self.imya = text[1]
            self.otchestvo = text[2]
            self.data = text[3]
            self.nomerZachetki = text[4]


    def printInfo(self):
        print(f"ФИО: {self.familiya} {self.imya} {self.otchestvo}")
        print(f"Дата рождения: {self.data}")
        print(f"Номер ЗК: {self.nomerZachetki}")

class StudentsGroup:
    def __init__(self, file):
        self.Students = [Student(text=line) for line in file]

    def addStudent(self, familiya, imya, otchestvo, data, nomerZachetki):
        student = Student(familiya=familiya, imya=imya, otchestvo=otchestvo, data=data, nomerZachetki=nomerZachetki)
        self.Students.append(student)

    def removeStudent(self, index):
        self.Students.pop(index)
    
    def printStudents(self):
        for i in range(len(self.Students)):
            print("-" * 15 + f"{i + 1}" + "-" * 15)
            self.Students[i].printInfo()
    
    def studentsToString(self):
        strStutdents = ""
        for i in self.Students:
            strStutdents += f"{i.familiya} {i.imya} {i.otchestvo} {i.data} {i.nomerZachetki}"
            strStutdents += "\n"
        return strStutdents

    def find_students(self, nomerZachetki):
        for i in range(len(self.Students)):
            if self.Students[i].nomerZachetki == nomerZachetki:
                return i

    def SortedStudents_OnFam(self):
        self.Students.sort(key=lambda student: student.familiya)

    def SortedStudents_OnNum(self):
        self.Students.sort(key=lambda student: student.nomerZachetki)

def printMenu():
    print("\nМеню:")
    print("1) Вывести список группы;")
    print("2) Добавить студента;")
    print("3) Удалить студента;")
    print("4) Отсортировать список по фамилии;")
    print("5) Отсортировать список по номеру ЗК;")
    print("6) Загрузить все в файл;")

path = "Students.txt"
with open(path, mode="r", encoding="UTF8") as file:
    contentFile = file.readlines()
    ivt_21_22 = StudentsGroup(contentFile)

choice = 123
while choice != "0":
    printMenu()
    choice = input("Введите вариант меню: ")
    if choice == "1":
        ivt_21_22.printStudents()
    elif choice == "2":
        familiya = input("Введите фамилию: ")
        imya = input("Введите имя: ")
        otchestvo = input("Введите отчество: ")
        data = input("Введите дату рождения (дд.мм.гггг): ")
        nomerZachetki = input("Введите номер зачетной книжки: ")
        ivt_21_22.addStudent(familiya=familiya, imya=imya, otchestvo=otchestvo, data=data, nomerZachetki=nomerZachetki)
        print("\nСтудент добавлен!\n")
    elif choice == "3":
        nomerZachetki = input("Введите номер ЗК: ")
        ivt_21_22.removeStudent(ivt_21_22.find_students(nomerZachetki))
        print("\nСтудент удалён!\n")
    elif choice == "4":
        ivt_21_22.SortedStudents_OnFam()
        print("\nСписок отсортирован по фамилии!\n")
    elif choice == "5":
        ivt_21_22.SortedStudents_OnNum()
        print("\nСписок отсортирован по номеру ЗК!\n")
    elif choice == "6":
        with open(path, mode="w", encoding="UTF8") as file:
            file.write(ivt_21_22.studentsToString())
        print("\nДанные загруженны в файл!\n")
    elif choice == "0":
        print("\nДо свидания!")
    else:
        print("Неккоректный ввод!")