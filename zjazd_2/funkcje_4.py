# Ver 1 funkcja przyjmuje zmienna cena
# oraz nieokreśloną liczbę tekstów.
# W testachz zamienić $cena na wartość zmiennej cena
# Zwrócić złączony tekst każdy tekstw nowej linii
x = ["Ala ma $cena PLN.", "W sam raz na nartę za $cena PLN.", "To jest $cena test"]
kwargs = {"cena": 10}

def formatuj(*args, **kwargs):
    out = []
    for text in args:
        for k in kwargs:
            text = text.replace(f"${k}", str(kwargs[k]))
        out.append(text)
    return "\n".join(out)




# def test_formatuj():
#     assert formatuj(
#         'koszt $cena PLN',
#         'kwota $cena brutto',
#         cena = 10
#     ) == "koszt 10 PLN\nkwota 10 brutto"
#
#     assert formatuj(
#         'koszt $cena PLN',
#         'kwota $cena brutto',
#         'sumarycznie $cena',
#         cena=10
#     ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"


