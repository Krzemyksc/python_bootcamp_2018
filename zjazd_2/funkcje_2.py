# def wiecej_niz(napis, prog):
#     liczniki_liter = {}
#     wynik = set()
#     for litera in napis:
#         liczniki_liter[litera] = liczniki_liter.get(litera, 0) + 1
#
#     for key, value in liczniki_liter.items():
#         if value > prog:
#             wynik.add(key)
#     return wynik

def wiecej_niz(napis, prog):
    wynik = set()
    for litera in napis:
        litera.lower()
        if napis.count(litera)>prog:
            wynik.add(litera)
    return wynik






def test_więcej_niż_dla_pustego_napis():
    assert wiecej_niz("", 0) == set()


def test_więcej_niż_dla_nie_pustego_napisu():
    assert wiecej_niz("aaaaaabbbcc", 2) == {'a', 'b'}
