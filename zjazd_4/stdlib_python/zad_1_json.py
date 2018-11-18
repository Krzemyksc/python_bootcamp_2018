import json

pracownicy = []
action = input("Co chcesz zrobic [d - dodaj, w - wypisz]: ")
if action == "d":
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownik = {
        "Imię": imie,
        "Nazwisko": nazwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja": pensja,
    }
    pracownicy.append(pracownik)
    with open("pracownicy.json", 'w') as f:
        json.dump(pracownicy, f)
elif action == "w":
    print("Pracownicy: ")
    for i, pracownik in enumerate(pracownicy, start=1):
        print(
            f" - [{id_} {pracownik['imie']} {pracownik ['nazwisko']} - rok: {pracownik['rok_urodzenia']}, pensja: {pracownik['pensja']} PLN")
else:
    print("Dokonano złego wyboru")
