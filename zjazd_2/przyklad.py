# # słowniki
# ##ctrl + / komentarze
#
# my_dict = {
#     "pierwsza": "a",
#     "druga": "b"
# }
# my_dict['trzecia'] = 'c'
#
# d2 = dict()
# d2 = dict(['a', 1])
# print(my_dict['pierwsza'])
# print(my_dict.items())  # drukuje cał słownik, wszystkie pary
# print(my_dict.keys())  # drukuje klucze
# print(my_dict.values())  # drukuje wartości
#
# produkt1 = {'nazwa': "Koper", "cena": 3}
# produkt2 = {'nazwa': "Kasza", "cena": 1.99}
# produkty = [produkt1, produkt2]
# for p in produkty:
#     print(p['nazwa'])
#
# kwadraty = [x ** 2 for x in range(1, 101)]
# #to jest to samo co to:
# kwadraty = []
# for x in range(1, 101):
#     kwadraty.append(x**2)
# print(kwadraty)
#
# def foo2(*args):
#     print(args)

def podzielna_przez_2(x):
    return x % 2 == 0


# print(podzielna_prze_2(12))
# print(podzielna_prze_2(11))

y = lambda x: x % 2 == 0
print(y(2))
print(y(5))
print(y(4))


def wybierz(dane, warunek):
    out = []
    for element in dane:
        if warunek(element):
            out.append(element)
    return (out)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 122, 123, 124]
print(wybierz(lista, podzielna_przez_2))
print(wybierz(lista, podzielna_przez_2))


def podzielna_przez_3(x):
    return x % 3 == 0
