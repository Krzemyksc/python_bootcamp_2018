# Cena_za_kilogram = 10.0
# Waga = 2.5
# Należność = (Cena_za_kilogram * Waga)
#
# out = f"""Cena za kg : {Cena_za_kilogram}
# waga: {Waga}
# Należność = {Należność}"""
#
# print(out)

def naleznosc(cena_za_kilogram, waga):
    cena = cena_za_kilogram * waga
    return cena


def rachunek(cena_za_kilogram, waga):
    print(f"""
        Cena za kilogram: {cena_za_kilogram}
        waga: {waga}
        należność: {naleznosc(cena_za_kilogram, waga)}""")


rachunek(5,5)

# print(naleznosc(10,2.5))
#
#
#
# def test_naleznosc():
#     assert naleznosc(5*5) == 25
