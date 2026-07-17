class Vector :
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def sum(self , v):
        return Vector((self.x + v.x) , (self.y + v.y))
    
    def print_vector(self):
         print(f"X is {self.x} and Y is {self.y}")
    
    def __add__(self , v):
        return Vector((self.x + v.x) , (self.y + v.y))

v1 = Vector(1,2)
v2 = Vector(10,25)

v = v1.sum(v2)
v.print_vector()