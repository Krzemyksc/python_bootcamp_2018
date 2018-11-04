LICZBA_DNI_TYGODNIA = 7

numer_dnia = 1
suma_temperatur = 0

min_ = None
max_ = None

while numer_dnia <= LICZBA_DNI_TYGODNIA:
    temp = int(input(f"Podaj temperaturę z dnia {numer_dnia}"))
    numer_dnia += 1
    suma_temperatur += temp
    min_ = temp
    max_ = temp
else:
    if temp < min_:
        min_ = temp
    if temp > max_:
        max_ = temp

srednia_temeratur = suma_temperatur / LICZBA_DNI_TYGODNIA
print(f'Srednia temperatura w tygodniu to {srednia_temeratur}')
print(f'Temperatura minimalna:{min_}')
print(f'Temperatura maksymalna:{max_}')
