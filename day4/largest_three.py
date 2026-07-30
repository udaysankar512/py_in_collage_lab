number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2:
    if number1>number3:
        print("The number ",number1, " is bigest .")
    else:
        print("The number ",number3, " is the bigest .")
else:
    if number2>number3:
        print("The number ",number2," is the bigest ")
    else:
        print("The number ",number3," is the bigest ")