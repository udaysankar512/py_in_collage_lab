#1. wriht a python program to remove all negitive numbers from a list without creating a new list.

numbers = [10,-5,20,-8,30,-2,40]
i = 0
print("list befor removing the negative numbers :",numbers)
while i < len(numbers):
   if numbers[i] < 0:
        numbers.pop(i)
   else:
     i+=1

print("list after removing the negative numbers :",numbers)