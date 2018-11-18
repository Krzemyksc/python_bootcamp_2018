# Mój sposób
# import csv
#
# with open("dane/titanic_train.csv") as csvfile:
#     data = csv.reader(csvfile,delimiter=",")
#     dlugosci = set()
#     zgon = 0
#     zyje = 0
#     for row in data:
#         if row[1] == "0":
#             zgon +=1
#         elif row[1] == "1":
#             zyje += 1
#     print("zgon" ,zgon)
#     print("zyje" ,zyje)



#aby eksportować do power pointa pip install python-pptx


# 2 sposób
import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    dlugosci = {}
    for row in data:
        dlugosci[row['Survived']] = dlugosci.get(row['Survived'], 0) + 1 # 0 mówi o tym, że jak nie znalazlłęś tego w słowniku to zwróc  wartość 0 ale jak doda się 1 to policzy to jako pierwsze wystąpienie
    #ogólem przeżywalnośc
    przezylo = dlugosci['1']
    zginelo = dlugosci['0']

    print(f"Przeżyło z ogółu {round(100*przezylo/(przezylo + zginelo), 2)}")
    kobiety = {}
with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    for row in data:
        if row['Sex'] == 'female':
            kobiety[row['Survived']] = kobiety.get(row['Survived'], 0) + 1 # 0 mówi o tym, że jak nie znalazlłęś tego w słowniku to zwróc  wartość 0 ale jak doda się 1 to policzy to jako pierwsze wystąpienie
    #ogólem przeżywalnośc
    przezylo = kobiety['1']
    zginelo = kobiety['0']

    print(f"Przeżyło z ogółu {round(100*przezylo/(przezylo + zginelo), 2)}")














