# słowniki
##ctrl + / komentarze

my_dict = {
    "pierwsza": "a",
    "druga": "b"
}
my_dict['trzecia'] = 'c'

d2 = dict()
d2 = dict(['a', 1])
print(my_dict['pierwsza'])
print(my_dict.items())  # drukuje cał słownik, wszystkie pary
print(my_dict.keys())  # drukuje klucze
print(my_dict.values())  # drukuje wartości

produkt1 = {'nazwa': "Koper", "cena": 3}
produkt2 = {'nazwa': "Kasza", "cena": 1.99}
produkty = [produkt1, produkt2]
for p in produkty:
    print(p['nazwa'])

kwadraty = [x ** 2 for x in range(1, 101)]
#to jest to samo co to:
kwadraty = []
for x in range(1, 101):
    kwadraty.append(x**2)
print(kwadraty)
