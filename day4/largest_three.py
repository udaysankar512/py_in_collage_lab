number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    print("The number", number1, "is the biggest among the three!")
elif number2 >= number1 and number2 >= number3:
    print("The number", number2, "is the biggest among the three!")
elif number3 >= number1 and number3 >= number2:
    print("The number", number3, "is the biggest among the three!")
else:
    print("All are the same numbers!")
