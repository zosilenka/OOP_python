# python3

# example of python inheritace
# version 1.0.1

class Animal:
    def __init__(self, imie):
        self.imie = imie
        self.glos = "aaaa"

    def eat(self):
        print("Niam niam niam")
    def dajglos(self):
        print(self.glos)
    def dajimie(self):
        print(self.imie)

class Horse(Animal):
    def galopuj(self):
        print("patataj")
    def dajglos(self):
        print("ihahaha")

class Dog(Animal):
    def gryz(self):
        print("ahrr")
    def dajglos(self):
        print("hauhauhau")

stella = Horse("stella")
blake = Dog("blake")

ferma = [Dog("Azor"), Dog("Axel"), Dog("Exel"), blake, Dog("ugryź"), stella, Horse("Gałka"), Horse("Piotruś")]
for zwierz in ferma:
    zwierz.dajimie()
    zwierz.dajglos()
    print("_____")



