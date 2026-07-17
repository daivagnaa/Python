numbers = [1 , 2 , 3 , 4 , 5]
print(numbers)
print(numbers[2:4])
print(numbers[3])
numbers.append(6)
print(numbers)
numbers.pop(2)
print(numbers)
numbers.insert(2,8)
print(numbers)
numbers.sort()
print(numbers)

marks = [99 , 100 , 94]
print(sorted(marks))

print("Table of 5 : ")
table = []

for i in range (1, 11):
    table.append(5*i)

print(table)

#ShortCut
table = [10*i for i in range (1, 11)]
print(table)