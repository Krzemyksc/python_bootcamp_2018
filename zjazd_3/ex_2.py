# class Employee:
#     time = 0
#
#     def __init__(self, imie, nazwisko, stawka, bonus):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.stawka = stawka
#         self.worked_hours = 0
#
#
#     # def employee(self, Imie, Nazwisko, stawka):
#     #     print(f"'{Imie}', '{Nazwisko}', '{salary}'")
#
#     def pay_salary(self):
#         self.to_pay = self.worked_hours * self.stawka
#         self.worked_hours = 0
#         return self.to_pay
#
#     def register_time(self, hours):
#         self.worked_hours += hours
#
#     # def overhours(self):
#     #     if self.worked_hours > 8:
#     #         self.Overhours = self.worked_hours - 8
#     #     self.Overhours_pay = self.Overhours * 2 * self.stawka
#     #     return self.Overhours_pay
#
# class PremiumEmployee(Employee):
#
#
#     def give_bonus(self, amount):
#         self.bonus = amount
#
#
#
#
#
# def test_employee():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert employee.imie == "Jan"
#     assert employee.nazwisko == "Nowak"
#     assert employee.stawka == 100.0
#
# def test_employee_pay_salary_with_no_worked_hours():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert employee.pay_salary() == 0
#
# def test_employee_pay_salary_with_worked_hours():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time() == 5
#     assert employee.pay_salary() == 500
#     assert employee.pay_salary() == 0
#
# def test_give_bonus():
#     employee = PremiumEmployee('Jan', 'Nowak', 100.0)
#     employee.register_time(5)
#     employee.give_bonus() == 1000.0
#     assert employee.pay_salary == 1500.0


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = set()
    def add_employee(self, employee):
        self.employees.add(employee)


    def size(self):
        return len(self.employees)

    def pay_all_salary(self):
        sum_ = 0
        for e in self.employees:
            sum_ += e.pay_salary()
