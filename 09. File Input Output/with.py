# f = open("dev.txt" , "r")
# content = f.read()
# print(content)
# f.close()
with open("dev.txt" , "r") as f:
    content = f.read()
    print(content)
    # No Need to write f.close()