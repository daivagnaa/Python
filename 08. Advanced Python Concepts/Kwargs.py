def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} are {kwargs[item]}")

marks(dev=100 , mohi=99 , kohli=101)