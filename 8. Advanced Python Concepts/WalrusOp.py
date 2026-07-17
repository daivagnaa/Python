def very_slow():
    print("Yeahhhhh.......")
    print("Yeahhhhh.......")
    print("Yeahhhhh.......")
    print("Yeahhhhh.......")
    print("Yeahhhhh.......")
    print("Yeahhhhh.......")
    return 18

if((a:=very_slow())>10):
    print(a)

else:
    print("Its not greater than 10")

while(data:= input("Enter Value : ")):
    print(data)
    if data == "q":
        break