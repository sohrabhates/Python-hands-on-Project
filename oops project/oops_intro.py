class Employee:
    company = "HP"

    def get_salary(self):  #self is important here because self is a away to refernce the oject of the class1
        return 34000
    
e = Employee()
print(e.get_salary())

e2 = Employee()
print(e2.get_salary())
