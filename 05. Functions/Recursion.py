#fibonacci

def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-2) + fib(n-1)

print (fib(6))
    
def fact(m):
    if (m==0 or m==1):
        return m
    return m * fact(m-1)

a = int(input("Enter Number to find Factorial : "))
print(f"Factorial of {a} is {fact(a)}")