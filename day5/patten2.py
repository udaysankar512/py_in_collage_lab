# b.
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

row = int(input("Enter the row :"))
while row > 0:
    for  i in range(1,row+1):
        print(i,end=" ")
    print()
    row-=1