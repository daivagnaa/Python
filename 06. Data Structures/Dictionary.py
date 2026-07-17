marks = {"Harry": 34 , "Jacks":45, "Dev": 100}
print(marks,type(marks))
print(marks["Dev"])

marks["Harry"] = 2
print(marks["Harry"])

print(marks.keys())
print(marks.values())

table = {i :5*i for i in range (1, 11)}
print (table)