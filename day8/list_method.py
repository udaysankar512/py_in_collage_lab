# Q .3 :- write a python program to exhibit the use of 'extend()' and 'append()' function in connection to list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1)
print(list2)

list1.append(4)
print("After append:", list1)

list1.extend(list2)
print("After extend:", list1)
