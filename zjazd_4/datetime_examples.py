import datetime

now = datetime.datetime.today()

print(now)
print(now.day)
print(now.year)
print(now.weekday())

x = datetime.datetime.strptime("2018-11-18", "%Y-%m-%d")
print(x)

my_birthday = datetime.datetime(1996, 9, 11)
print(my_birthday.weekday())
print(now > my_birthday)

for i in range(20):
    print(now + datetime.timedelta(weeks=i))#przypominajka co tydzień

print("Dni od narodzin:",now - my_birthday)