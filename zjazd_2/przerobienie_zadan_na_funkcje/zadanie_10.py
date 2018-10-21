def pobranie_danych():
    liczba_1 = int(input("Podaj pierwsza liczbę: "))
    liczba_2 = int(input("podaj liczbę drugą: "))
    operacja = input("Rodzaj operacji: ")
    return liczba_1, liczba_2, operacja
def kalkulator(liczba_1, liczba_2, operacja):
    if operacja == "+":
        wynik = liczba_1 + liczba_2
    elif operacja == "-":
        wynik = liczba_1 - liczba_2
    elif operacja == "/":
        if liczba_2 == 0:
            raise ValueError("Cholero nie dziel przez 0")
        wynik = liczba_1 / liczba_2
    elif operacja == "*":
        wynik = liczba_1 * liczba_2
    else:
        print("zła operacaja")
        #raise ValueError("Nieprawidłowa wartość dla parametru typ operacji")
    print("wynik operacji: ",wynik)

def prezentuj_wynik():
    dane = pobranie_danych()
    try:
        wynik = kalkulator(*dane)
    except:
        wynik = "Operacja niedozwolona"
    print(wynik)
prezentuj_wynik()

# def kalkulator (a, b, operacja = ""):
#     if operacja == "+":
#         wynik = a + b
#     elif operacja == "-":
#         wynik = a - b
#     elif operacja == "/":
#         if b == 0 or a == 0:
#             raise ValueError("Cholero nie dziel przez 0")
#         wynik = a / b
#     elif operacja == "*":
#         wynik = a * b
#     else:
#         print("zła operacaja")
#     return wynik
# print(kalkulator(2,2,"*"))
