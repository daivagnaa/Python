try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print ("Mode of Operation\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
    
    o = int(input("Enter the operation you want to perform (1-4): "))

    match o:
        case 1:
            print(f"The sum of {a} and {b} is: {a + b}")
        case 2:
            print(f"The difference of {a} and {b} is: {a - b}")     
        case 3:
            print(f"The product of {a} and {b} is: {a * b}")
        case 4:
            try:
                print(f"The division of {a} by {b} is: {a / b}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        case default:
            print("Invalid operation selected. Please choose a number between 1 and 4.")
except Exception as e:
    print("Please enter valid integers.")
    
