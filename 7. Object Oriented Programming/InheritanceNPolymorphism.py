class Animal:
    location = "India"
    def __init__(self , name):
        self.name = name
    def speak(self):
        print("Bhau Bhau")

class Dog(Animal): #Dog class inherits Animal class (Child : Dog , Parent : Animal)
    def speak(self):
        super().speak()
        print("Woof!")

a = Dog("Bruno")
a.speak()
print(a.location)
print(a.name)
