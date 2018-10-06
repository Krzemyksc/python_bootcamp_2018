



miasto_A = input("podaj miasto wyjazdu")
miasto_B = input("podaj cel podróży")
Dystans = int ( input( f"Podaj dystans między {miasto_A} - {miasto_B}: "))
Cena_paliwa = float (input("Podaj cene paliwa: "))
spalanie = float( input("spalanie na 100 km: "))

koszt =int((Dystans/100) * spalanie * Cena_paliwa)

output = f'''
Miasto a : {miasto_A}
Miasto b : {miasto_B}
dystans : {Dystans}
spalanie na 100 : {spalanie}
Koszt przejazdu : {miasto_A} - {miasto_B} to {koszt} PLN'''
print(output)





