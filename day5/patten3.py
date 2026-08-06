# c.
# A B C D E 
# A B C D  
# A B C  
# A B 
# A 

# we print the patten using the ASKI values 

row = int(input("Enter the row numbers : "))
while row > 0:
    for i in range(row):
        print(chr(65+i),end=" ")
    print()
    row -= 1