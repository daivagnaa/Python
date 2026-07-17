class Employee:
    company = "Google"

    def get_salary(self):
        return 34000
    
e = Employee() #Object of class Employee
print(e.get_salary()) # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)