import argparse

parser = argparse.ArgumentParser(description= "Simple Calculator")

parser.add_argument("Num1" , type=float , help="First Number")
parser.add_argument("Num2" , type=float , help="Second Number")
parser.add_argument("operation" , choices=["add" , "sub" , "mul" , "div"] , help="operation to perform")

args = parser.parse_args()

# print(args)

if(args.operation == "add"):
    print(f"The result is {args.Num1 + args.Num2}")
elif(args.operation == "sub"):
    print(f"The result is {args.Num1 - args.Num2}")
elif(args.operation == "mul"):
    print(f"The result is {args.Num1 * args.Num2}")
elif(args.operation == "div"):
    print(f"The result is {args.Num1 / args.Num2}")
else:
    print("Some error Occured")