class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"Name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")


e1 = Employee(34000, "John Doe", 6)

print(e1.salary)          # Directly access attribute
print(e1.get_salary())    # Using method
e1.get_info()