X = int(input("Podaj pozycje gracza X: "))
Y = int(input("Podaj pozycje gracza Y: "))
if X > 100 or Y > 100:
    print("poza plansza")
elif X <= 10 and Y <= 10:
    print("Lewy dolny róg")
elif X >= 90 and Y <= 10:
    print("Prawy dolny róg")
elif X <= 10 and Y >= 90:
    print("lewy górny róg")
elif X >= 90 and Y >= 90:
    print("prawy górny róg")
elif X > 10 and X < 90 and Y < 10:
    print("dolna krawędź")
elif X > 10 and X < 90 and Y > 90:
    print("górna krawędź")



