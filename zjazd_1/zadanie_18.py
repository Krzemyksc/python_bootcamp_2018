# stworzyć  listę z liczbami od 0 do 100
lista = list(range(101))

wynik = []

for el in lista:
    if el % 3 == 0 or el % 5 == 0:
        wynik.append(el)
print("Liczby podzielne przez 5 i 3")
print()
for el in wynik:
    print(el)

print(f"W przedziale od 100 do 0 jest {len(wynik)} liczb podzielnych przez 3 lub 5")
