liczby = [5, 2, 1, 4, 3]
min_i = None
max_i = None
indeksy = list(range(len(liczby)))
for i in range(len(liczby)):
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i
    tmp = liczby[min_i]
    liczby[min_i] = liczby[max_i]
    liczby[max_i] = tmp
print(liczby)
assert liczby == [1,2,5,4,3]



#sposób
liczby[min_i], liczby[max_i] = liczby[max_i], liczby[min_i]