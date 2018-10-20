print("Wstaw dowolny napis: ", end='')
napis = input("")
a, e, i, o, u, y = [], [], [], [], [], []
for x in napis:
    if x == "a":
        a.append(x)
    if x == "e":
        e.append(x)
    if x == "i":
        i.append(x)
    if x == "o":
        o.append(x)
    if x == "u":
        u.append(x)
    if x == "y":
        y.append(x)

print(f"Ilość a: {len(a)}")
print(f"Ilość e: {len(e)}")
print(f"ilośc i: {len(i)}")
print(f"Ilość o: {len(o)}")
print(f"Ilość u: {len(u)}")
print(f"Ilość y: {len(y)}")