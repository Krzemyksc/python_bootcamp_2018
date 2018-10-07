lista = [-1, 2, -3, -5, -6, 100, -500, 0]

# 1. liczniki
licznik_ujemnych = 0
licznik_dodatnich = 0
for el in lista:
    if el < 0:
        licznik_ujemnych += 1
    elif el > 0:
        licznik_dodatnich += 1
print(f"Dodatnie: {licznik_dodatnich}")
print(f"ujemne: {licznik_ujemnych}")
