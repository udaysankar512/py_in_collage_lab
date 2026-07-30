# (c).
# 1
# 2 3
# 4 5 6
# 7 8 9 10

row=int(input("Enter the number of colom you want in the patten :"))
ref=0
for i in range(row+1):
    for j in range(i):
        ref+=1
        print(ref,end=" ")
    print()
