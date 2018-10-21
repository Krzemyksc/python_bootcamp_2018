a = int(input("Podaj długość w cm: "))
b = int(input("Podaj szerokosc w cm: "))
c = int(input("podaj glebokosc w cm: "))
d = int(a * b * c)
if d > 1000:
    print(f"Wiecej niż litr")
else:
    print(f"Mniejsze lub równe litr")
