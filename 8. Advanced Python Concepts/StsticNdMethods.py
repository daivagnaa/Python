class Employee:
    company = "Asus"
    def __init__(self , name , salary):
        self.name = name 
        self.salary = salary

    def print_info(self):
        print (f"The name is {self.name} and the salary is {self.salary}")

    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def change_com(cls , new_com):
        cls.company = new_com
        
e1 = Employee("Dev" , 500000)
e2 = Employee("Mohit" , 600000)
print(Employee.company)
print(e1.name)
e1.print_info()
e2.print_info()
print(e2.sum(5,18)) #Static methods doesn't use instance attribute
print(Employee.company)
e1.change_com("Acer")
print(Employee.company)