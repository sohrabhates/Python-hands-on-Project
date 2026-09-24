class Employee:
    company = "Asus"

    def __init__(self, salary, name, bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"Name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(40000, "john", 5, "Tesla")
print(e1.company)  # Accessing class variable
print(e1.company)
#Object introspection
# print(dir(e1))