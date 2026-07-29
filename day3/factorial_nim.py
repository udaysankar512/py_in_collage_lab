#2. write a python code to find the factorial of a given number .

number=int(input("Enter a number for factorial :"))
factorial=1
if number<0:
    print("Sorry, factorial does not exist for negative numbers")
elif number==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial*=i
    print("The factorial of", number, "is", factorial)