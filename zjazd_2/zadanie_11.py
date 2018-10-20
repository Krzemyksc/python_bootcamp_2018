liczby = set()
while True:
    komenda = input("Podaj liczbę lub k aby zakończyć: ")
    if komenda == 'k':
        break
    liczby.add(int(komenda))

print(len(liczby &(set(range(2, 101, 2)))))
