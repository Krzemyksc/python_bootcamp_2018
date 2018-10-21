# pobieranie daych
def pobieranie_danych():
    miasto_A = input("podaj miasto wyjazdu")
    miasto_B = input("podaj cel podróży")
    Dystans = int(input(f"Podaj dystans między {miasto_A} - {miasto_B}: "))
    Cena_paliwa = float(input("Podaj cene paliwa: "))
    spalanie = float(input("spalanie na 100 km: "))
    return miasto_A, miasto_B, Dystans, Cena_paliwa, spalanie


# obliczenie kosztu
def obliczanie_kosztu(miasto_A, miasto_B, Dystans, Cena_paliwa, spalanie):
    koszt = int((Dystans / 100) * spalanie * Cena_paliwa)
    return koszt


dane = pobieranie_danych()
koszt = obliczanie_kosztu(*dane)
print(koszt)


def drukuj_wynik(miasto_A, miasto_B, Dystans, Cena_paliwa, spalanie):
    koszt = obliczenie_kosztu(Dystans, Cena_paliwa, spalanie)
    output = f'''
       Miasto a : {miasto_A}
       Miasto b : {miasto_B}
       dystans : {Dystans}
       spalanie na 100 : {spalanie}
       Koszt przejazdu : {miasto_A} - {miasto_B} to {koszt(Dystans, spalanie, Cena_paliwa)} PLN'''
    print(output)

    # # #prezentowanie danych
    # # def drukuj(dane):
    # output = f'''
    # Miasto a : {miasto_A}
    # Miasto b : {miasto_B}
    # dystans : {Dystans}
    # spalanie na 100 : {spalanie}
    # Koszt przejazdu : {miasto_A} - {miasto_B} to {koszt(Dystans, spalanie, Cena_paliwa)} PLN'''
    # print(output)
