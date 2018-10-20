# a = input("Co chcesz kupić: ")
#
# my_dict = {
#     'nazwa': "ziemniaki", "cena za kilogram": 3
# }
# produkty = [my_dict]
# rachunek = 0
#
# for p in produkty:
#     p = int(input("Podaj ilość kilogramów: "))
#     rachunek = my_dict[a] * p
#
# print(rachunek)

produkty = {"ziemniaki": 2, "bataty": 4, "pomidory": 6}
magazyn = {"ziemniaki": 10, "bataty": 10, "pomidory": 10}
do_zaplaty = 0
while True:
    print("-" * 40)
    print("Nasz zielnik oferuje: ")

    for produkt in produkty:
        # cena = produkty[produkt]
        print(f' - {produkt} - {produkty[produkt]} PLN')
    print()
    komenda = input("Co chcesz zrobić: [k]upic,[d]odać ,[koniec] by przerwać zakupy: ")
    if komenda == 'koniec':
        break
    elif komenda == 'k':
        produkt_wybrany = input("Co chcesz kupic? ")
        if produkt_wybrany not in produkty:
            print("Nie mamy takiego produktu!!!")
            continue
        waga = float(input(f"Ile chcesz kupic wybranego produktu [{produkt_wybrany}]: "))
        if magazyn[produkt_wybrany] < waga:
            print(f"Mamy za mało {produkt_wybrany}, mamy {magazyn[produkt_wybrany]}")
            continue
        magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga
        cena = produkty[produkt_wybrany]
        koszt = waga * cena
        do_zaplaty += koszt
    elif komenda == 'd':
        #dodawanie do magazynu
        produkt_do_dodania = input("Jaki produkt chcesz dodać? ")
        ile_produktu_dodajemy = float(input("Ile tego dodać"))
        magazyn[produkt_do_dodania] += ile_produktu_dodajemy
        if produkt_do_dodania not in magazyn:
            magazyn[produkt_do_dodania] = 0
            cena_nowego_produktu = float(input("Za ile to sprzedajemy? "))
            produkty[produkt_do_dodania] = cena_nowego_produktu
    else:
        print("Niepoprawana komenda!!!")

print(f"Wyliczony koszt to: {do_zaplaty}")
