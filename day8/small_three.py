# Q .2 :- write a python progrem to find the smallest of three numbers using nested if-else ststment.

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))

if num1 < num2:
    if num1 < num3:
        print("The smallest number is :",num1)
    else:
        print("The smallest number is :",num3)
else:
    if num2 < num3:
        print("The smallest number is :",num2)
    else:
        print("The smallest number is :",num3)

