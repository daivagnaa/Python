class Student:
    def __init__(self , name , number ):
        self.name = name
        self.number = number

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    @first_name.setter
    def first_name(self , first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

    
s = Student("Dev Parmar" , 19)
# print(s.first_name())
# s.set_first_name("Daivagna")
# print(s.name)
# s.projects = 6
# print(s.projects)

print(s.first_name)
s.first_name = "Daivagna"
print(s.name)