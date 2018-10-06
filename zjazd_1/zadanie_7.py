liczba = int(input("Podaj liczbe: "))

podzielna_przez_2 = liczba % 2 == 0
podzielna_przez_3 = liczba % 3 == 0
wieksza_niż_10 = liczba > 10
rowna_7 = liczba == 7



print(podzielna_przez_2, podzielna_przez_3, wieksza_niż_10, rowna_7)
wynik = (podzielna_przez_2 and podzielna_przez_2 and wieksza_niż_10 or rowna_7)
print(wynik)