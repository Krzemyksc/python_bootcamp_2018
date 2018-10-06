liczba_1 = int(input("Podaj pierwsza liczbę: "))
liczba_2 = int(input("podaj liczbę drugą: "))
operacja = input("Rodzaj operacji: ")
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
