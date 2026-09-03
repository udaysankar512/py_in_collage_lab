# Q .2 :- write a python progrem to find the smallest of three numbers using nested if-else ststment.

def smallest(nu1,nu2,nu3): 
    if nu1 < nu2:
      if nu1 < nu3:
        return nu1
      else:
        return nu3
    else:
        if nu2 < nu3:
            return nu2
        else:
            return nu3

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))

result = smallest(num1,num2,num3)

print("The smallest number is :",result)