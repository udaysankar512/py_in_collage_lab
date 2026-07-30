# (b).
# 1
# 2 2
# 3 3 3
# 4 4 4 4

row=int(input("Enter the number of colom you want in the patten :"))
for i in range(row+1):
    for j in range(i):
        print(i,end=" ")
    print()
