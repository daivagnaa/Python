class Employee:
    def __init__(self , salary , name , bond):
            self.salary = salary
            self.name = name
            self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
         print(f"The name of Employee is {self.name} , Salary is {self.salary} and The Bond is for {self.bond} Years")

e1 = Employee(340000 , "Daivagna" , 4)
print(e1.get_salary())
e1.get_info()