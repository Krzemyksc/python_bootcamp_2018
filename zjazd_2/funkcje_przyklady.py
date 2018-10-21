# # def przywitaj_się():
# #     return 1
# #
# #
# # print(przywitaj_się())
#
#
# def przywitaj_sie(imie):
#     print("Witaj", imie)
#
# lista_imion = ['Rafał', 'Adam', 'Agnieszka']
#
# for imie in lista_imion:
#     przywitaj_sie(imie)

# def przywitaj_sie(imie,wiek,waga,wzrost):
#     print("Witaj", imie)

#
#  lista_osob = [
#     {'imie': "Mateusz",
#     'wiek': 38,
#      'wzrost': 178,
#      'waga' : 102,
#     },
#     {'imie': "Adam",
#     'wiek': 40,
#      'wzrost': 178,
#      'waga' : 80,
#     },
#     {'imie': "ada",
#     'wiek': 38,
#      'wzrost': 185,
#      'waga' : 70,
#     }
# ]
# for osoba in lista_osob:
#     przywitaj_sie(osoba['imie'],osoba)

def drukuj_linie():
    print("-" * 40)


def zwroc_wartosc_wpisana():
    wartosc = input("Podaj Wartosc")
    return wartosc





x = zwroc_wartosc_wpisana()
drukuj_linie()
