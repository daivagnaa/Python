while True:
    try:
        a = int(input("Enter a number : "))
        b = int(input("Enter another number : "))
        print(f"Divsion : {a/b}")
    except ZeroDivisionError:
        print("Do not divide by Zero")
    except Exception as e:
        print("Some error Occured !",e)
   
c = int(input("Enter a number : "))
d = int(input("Enter another number : "))

if d==0 :
    raise ValueError ("Do not divide by Zero")

print(f"The division is {a/b}")