print([i / 10 for i in range(0, 11)])

tupli = {(x, x ** 2, x ** 3) for x in range(-10, 11)}

print(tupli)

zbior_napisow ={'abc', 'ala ma kota', 'slowacki wielkim poeta był', 'Superman'}
print({x:len(x) for x in zbior_napisow})
