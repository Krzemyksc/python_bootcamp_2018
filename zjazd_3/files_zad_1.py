import sys

if len(sys.argv) > 1:
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku) as f:

        for i, line in enumerate(f, start=1):
            print(1, line, end="")

else:
    print(input("Podaj nazwe pliku"))