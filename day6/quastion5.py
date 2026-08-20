# 5. write a python program to swap the values of two variables using tuple unpacking using a lemporary third variable.

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = (b,a)

a, b = temp

print("After swapping:")
print("a =", a)
print("b =", b)