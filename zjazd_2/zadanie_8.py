my_text = input("Podaj tekst: ")
czy_miedzy_nawiasami = False
licznik = 0

for znak in my_text:
    if znak == "<":
        czy_miedzy_nawiasami = True
    elif znak == ">":
        czy_miedzy_nawiasami = False
    elif czy_miedzy_nawiasami:
        licznik += 1

print(licznik)
