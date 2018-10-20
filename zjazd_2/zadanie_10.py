# # w podanym napisie zliczyć wystąpienia poszczególnych liter

#     print(litera)
#     if litera not in licznik_liter:
#         licznik_liter = licznik_liter.get(litera)
#     elif litera in licznik_liter:
#         licznik_liter = licznik_liter
#
#
# print(licznik_liter.items())

napis = input("Podaj napis: ")
liczniki_liter = {}
#zliczyć
##sposób 1
# for litera in napis:
#     if litera in liczniki_liter:
#         liczniki_liter[litera] += 1
#     elif litera in liczniki_liter:
#         liczniki_liter[litera] = 1
##sposób 2
for litera in napis:
    liczniki_liter[litera]= liczniki_liter.get(litera, 0) + 1
# wyświetlić
for litera in napis:
    print(f"Litera: {litera}, wystąpiła{liczniki_liter[litera]} razy")
