# def is_greater (x):
#     if x>9:
#         return True
#     else:
#         return False
a = [1 , 2 , 5 , 6 , 7 , 10 , 18]
new = list(filter(lambda x: x>9 , a))
print(new)