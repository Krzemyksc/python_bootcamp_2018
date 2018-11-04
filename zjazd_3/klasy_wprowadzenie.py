class Animal:  # tworzenie klasy, definicja klasy
    nazwa = "Fauna" # atrybut klasowy
    licznik = 0

    def _init_(self, gatunek):  # self to wskaznie na konkretną instancję, pierwszy argument w definicji kalsy musi wskazywać na instancje
        self.gatunek = gatunek  # atrybuty instancji, obiektu
        self.licznik += 1

    def _str_(self):
        return "Animal"


azor = Animal("pies")  # tworzenie instancji danej klasy
rudolf = Animal("Rangifer tarandus")
# print(azor)  # reprezentacja napisowa instancji klasy
# print(dir(azor))
print(azor.gatunek)  # wypisanie atrybutu
print(rudolf.gatunek)
