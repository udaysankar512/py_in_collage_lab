# Q .1 :- write a python program to find the vallue of 'x^y', where values of 'x' and 'y' are to be given by the user. Use loops hear to solve the problem.

nums = int (input("Enter the number :"))
power = int (input("Enter the power of the number :"))
solv = 1
for i in range(power):
    solv *= nums

print("The result is :",solv)