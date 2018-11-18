import json
#W kontekście json to co jest miedzy nawaisami klamrowymi jest obiektem
# tworzę pythonowy obiekt

meble = ["krzesła", "szafa", "komoda", "stół"]
print(type(meble))

meble_as_json = json.dumps(meble)
print(type(meble_as_json))
print(meble_as_json)

odczytane_z_json_meble = json.loads(meble_as_json)
print(type(meble_as_json))
print(odczytane_z_json_meble)

with open("meble.json", "w") as f:
    json.dump(meble, f)

with open("meble.json") as f:
    meble = json.load(f)
    meble.append("taboret")
print(meble)

with open("meble.json", "w") as f: # "w" ozancza że można odczytać i zapisać plik a dokąnie to nadpisać bo ono zawsze nadpisuje
    json.dump(meble, f)

#dump potrzebuje obiektu do serializacji i pliku do którego chcesz to zrobić
# a dumps bierze obiekt i robi z niego napis
# loads wie ze będzie pracowac na napisie
# a load spodziewa się że będzie pracowac na pliku po użyciu nie ważne jakiego load mam obiekt pythonowy a nie napis

from collections import namedtuple

B = namedtuple("B", ["a", "b"])

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = A(1, 2)
b = B(1, 2)

print(json.dumps(a.__dict__))
print(json.dumps(b))

# try i except - rzucenie błędu wyjątek