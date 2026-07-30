number=int(input("Enter a number :"))
sum=0
original=number
while number>0:
    digit=number%10
    sum+=digit
    number//=10
print("The sum of the number ",original," is : ",sum)