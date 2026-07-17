def add(a,b): #a and b are parameters
    return (a+b)

c = add(3,5) # 3 and 5 are arguments
print(c)

#default arguments

def sub(d , e , plus=0):
    x = d-e-plus
    return x

f = sub(10,4,2)
print(f)