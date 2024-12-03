class WorkerInThisWeek:

    def __init__(self, famWorker=None, countDetails=None, text=None):
        if text:
            listData = text.split()
            self.famWorker = listData[0]
            self.countDetails = [int(listData[x]) for x in range(1, len(listData))]
        elif famWorker and countDetails:
            self.famWorker = famWorker
            self.countDetails = countDetails

    def getMaxCount(self):
        return max(self.countDetails)

    def getMaxDay(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        max_index = self.countDetails.index(self.getMaxCount())
        return days[max_index]

    def summaDetails(self):
        return sum(self.countDetails)

    def __lt__(self, other):
        return self.famWorker < other.famWorker

########################################################################################################################

class WeekOfCeh:

    def __init__(self, file):
        self.Workers = [WorkerInThisWeek(text=line) for line in file]


    def addWorker(self, fam, CountDatails):
        worker = WorkerInThisWeek(fam, CountDatails)
        self.Workers.append(worker)


    def removeWorker(self, index):
        self.Workers.pop(index)


    def printWorkersProgress(self):
        for i in range(len(self.Workers)):
            print(f"{i + 1}" + "." * 40)
            self.Workers[i].printProgress()

    def printMaxProgressWorker(self):
        maximum = 0
        index = 0
        for i in range(len(self.Workers)):
            if (maximum <= self.Workers[i].getMaxCount()):
                maximum = self.Workers[i].getMaxCount()
                index = i

        print(f"{self.Workers[index].famWorker} - {self.Workers[index].getMaxDay()}")

    def WorkersToString(self):
        strWorkers = ""
        for i in self.Workers:
            strWorkers += f"{i.famWorker}"
            for x in i.countDetails:
                strWorkers += f" {x}"
            strWorkers += "\n"
        return strWorkers


    def SortedWorkers(self, key="fam"):
        if key == "fam":
            self.Workers.sort(key=lambda worker: worker.famWorker)
        elif key == "summa":
            self.Workers.sort(key=lambda worker: worker.summaDetails(), reverse=True)


########################################################################################################################
def printMenu():
    print("\nМеню:")
    print("1) Вывести список работников;")
    print("2) Вывести рекордсмена дня;")
    print("3) Добавить пользователя;")
    print("4) Удалить пользователя;")
    print("5) Отсортировать список;")
    print("6) Загрузить все в файл;")

path = "File.txt"
with open(path, mode="r", encoding="UTF8") as file:
    contentFile = file.readlines()
    Ceh = WeekOfCeh(contentFile)

choise = 123
while choise != "0":
    printMenu()
    choise = input("Введите вариант меню: ")
    if choise == "1":
        Ceh.printWorkersProgress()
    elif choise == "2":
        Ceh.printMaxProgressWorker()
    elif choise == "3":
        fam = input("Введите фамилию: ")
        count =[int(input(f"Введите кол-во собранных деталей в {i} день недели: ")) for i in range(1, 7)]
        Ceh.addWorker(fam, count)
    elif choise == "4":
        index = int(input("Введите id пользователя: "))
        Ceh.removeWorker(index - 1)
    elif choise == "5":
        sort_key = input("Введите тип сортировки (fam / summa): ").strip()
        Ceh.SortedWorkers(key=sort_key)
    elif choise == "6":
        with open(path, mode="w", encoding="UTF8") as file:
            file.write(Ceh.WorkersToString())
    elif choise == "0":
        print("\nДо свидания!")
    else:
        print("Неккоректный ввод!")
