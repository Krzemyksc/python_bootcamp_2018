#   0  1  2  3
#
#

print("  ", end='')
for x in range(10):#dla zmiennej tymczasowej x w tablicy indeksów od 0 do 10
    print(f"{x:3}", end='')#wykonaj trzy spacje
print()#zostaw pustą linię
print()#zostaw pusta linię

for x in range(10):#dla zmiennej tymczasowej x w tablicy indeksow od 0 do 10
    print(x, end='  ')# pokaż mi x nie robi żadnej spacji ale zaczbnij następną liniję od tego miejsca i zrób 3 spacje
    for y in range(10):
        print(f"{x*y:3}", end='')
    print()
