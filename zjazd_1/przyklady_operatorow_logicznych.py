a = int(input("podaj liczbe: "))
b = int(input("podaj liczbe: "))

# a > b i a pdozielne przez b
print(" Wytnik", a > b and a % b == 0)

# a większe od b lub a większe do 7


print(a > b or a > 7)

print(not a < 10)

if a > b and a % b == 0:
    print(f'liczba{a} jest większa od {b} i jest podzielna przez {b}')
elif a == b:
    print (f"liczba a jest równa b i wynosi: {a}")
else:
    print("Haha")
