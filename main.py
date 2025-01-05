class Employee:
    def __init__(self, hours_worked, rate, bonus_coeff):
        self.hours_worked = hours_worked
        self.rate = rate
        self.bonus_coeff = bonus_coeff

    def calculate_bonus(self):
        return self.hours_worked * self.rate * self.bonus_coeff

class SeniorEmployee(Employee):
    def __init__(self, hours_worked, rate, bonus_coeff, responsibility_level):
        super().__init__(hours_worked, rate, bonus_coeff)
        self.responsibility_level = responsibility_level

    def salary_to_hours_ratio(self):
        salary = self.hours_worked * self.rate + self.calculate_bonus()
        return salary / self.hours_worked if self.hours_worked > 0 else 0

class Director(Employee):
    def __init__(self, hours_worked, rate, bonus_coeff, department):
        super().__init__(hours_worked, rate, bonus_coeff)
        self.department = department

    def salary_to_hours_ratio(self):
        salary = self.hours_worked * self.rate + self.calculate_bonus()
        return salary / self.hours_worked if self.hours_worked > 0 else 0

employee = Employee(160, 20, 0.1)
print(f"Премия сотрудника: {employee.calculate_bonus()}")

senior = SeniorEmployee(160, 30, 0.15, "High")
print(f"Премия старшего сотрудника: {senior.calculate_bonus()}")
print(f"Соотношение зарплаты к рабочим часам: {senior.salary_to_hours_ratio()}")

director = Director(160, 50, 0.2, "Finance")
print(f"Премия директора: {director.calculate_bonus()}")
print(f"Соотношение зарплаты к рабочим часам: {director.salary_to_hours_ratio()}")
