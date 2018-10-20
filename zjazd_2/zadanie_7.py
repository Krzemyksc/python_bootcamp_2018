napis = input("Podaj napis: ")
ile_samoglosek = 0
SAMOGLOSKI = 'aeiou'
for znak in napis:
    if znak in SAMOGLOSKI:
        ile_samoglosek += 1
print(f"W tekscie: {napis}, znajduje sie {ile_samoglosek}")
