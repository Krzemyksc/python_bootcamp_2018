import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
print( "rates: ", rates)
for r in rates:
    print(f"- {r['code']} - {r['mid']}")

waluta = input("Jaka waluta z powyższej listy? ")
ile = float(input(f"Ile chcesz kpić {waluta}? "))

for r in rates:
    if r['code'] == waluta:
        result = ile * r['mid']
print('płacisz', result)