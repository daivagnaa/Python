def divide(a , b):
    try:
        c = a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("Always Executed")
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
divide(a , b)