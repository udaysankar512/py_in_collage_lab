# Q. creat a menu-driver program using match-case statment in python .
# basic calculter

def calculation():
    while True:
        print("Basic Operations ")
        print("Ente + for Addition")
        print("Enter - for Subctraction")
        print("Enter * for Multiplication")
        print("Enter / for Divition ")
        print("Enter 'E' for eaxit the loop")
        choise = input("Enter your choise : ")
        
        match choise:
            case '+':
                a = int(input("Enter the first number :"))
                b = int(input("Enter the second number :"))
                print("The sum is : ",a+b)
            case '-':
                a = int(input("Enter the first number :"))
                b = int(input("Enter the second number :"))
                print("The sum is : ",a-b)
            case '*':
                a = int(input("Enter the first number :"))
                b = int(input("Enter the second number :"))
                print("The Muitiplication is : ",a*b)
            case '+':
                a = int(input("Enter the first number :"))
                b = int(input("Enter the second number :"))
                if b !=0:
                    print("The Divition is : ",a/b)
                else:
                    print("Dividion is not valid !")
            case 'E':
                print("Thanks you for doing calculaction ")
                exit()
            case _:
                print(" You enter the rong input !")
                
calculation()