age = int(input("Enter Age : "))

if(age > 18):
    print("Driver")
elif(age == 18):
    print("Interview")
elif(age == 0):
    print("Just Born")
else:
    print("Can't Drive")