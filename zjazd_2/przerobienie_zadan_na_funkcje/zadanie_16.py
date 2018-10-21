# zebranie liczb ( nie więcej niż 10)
liczby = []
while len(liczby) < 10 :
    nowa_liczba = int(input("Proszę podać liczbę: "))
    liczby.append(nowa_liczba)

# obliczenie średniej
srednia = sum(liczby) / len(liczby)
# wypisanie wyniku
print(srednia)