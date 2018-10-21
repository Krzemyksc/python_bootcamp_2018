# LICZBA_DNI_TYGODNIA = 7
#
# numer_dnia = 1
# suma_temperatur = 0
#
# min_ = None
# max_ = None
#
# while numer_dnia <= LICZBA_DNI_TYGODNIA:
#     temp = int(input(f"Podaj temperaturę z dnia {numer_dnia}"))
#     suma_temperatur += temp
#     numer_dnia += 1
#     min_ = temp
#     max_ = temp
# else:
#     if temp < min_:
#         min_ = temp
#     if temp > max_:
#         max_ = temp
#
# srednia_temeratur = suma_temperatur / LICZBA_DNI_TYGODNIA
# print(f'Srednia temperatura w tygodniu to {srednia_temeratur}')
# print(f'Temperatura minimalna:{min_}')
# print(f'Temperatura maksymalna:{max_}')


# POBIERANIE DANYCH
def pobieranie_danych(ile_razy=7):
    temperatury = []
    for i in range(ile_razy):
        temp = int(input(f"Podaj temperaturę z dnia {i+1}: "))
        temperatury.append(i)
    return temperatury

def srednia_temp(temperatury):
    srednia_temperatura = sum(temperatury) / len(temperatury)
    return srednia_temperatura

def znajdz_ekstrema(temperatury):
    min_ = min(temperatury)
    max_ = max(temperatury)
    return min_, max_

def prezentuj_dane(srednia_temperatura, min_, max_):
    print(f'Srednia temperatura w tygodniu to {srednia_temperatura}')
    print(f'Temperatura minimalna:{min_}')
    print(f'Temperatura maksymalna:{max_}')

dane = pobieranie_danych()
sr_temp = srednia_temp(dane)
min_, max_ = znajdz_ekstrema(dane)
prezentuj_dane(sr_temp, min_, max_)