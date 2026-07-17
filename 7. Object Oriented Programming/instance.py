class Employee:
    company = "Asus" #Asus is class attribute will be printed onluy when no instance attribute is passed

    def __init__(self , salary , name , bond , company):
            self.salary = salary
            self.name = name
            self.bond = bond
            self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
         print(f"The name of Employee is {self.name} , Salary is {self.salary} and The Bond is for {self.bond} Years")

e1 = Employee(340000 , "Daivagna" , 4 , "Tesla")
print(e1.company) #Tesla is instance attribute amd will always be printed
print(Employee.company) #Prints class Atrribute

#Object introspection
print(dir(e1))