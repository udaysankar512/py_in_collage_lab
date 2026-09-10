# Q.4. Write a program that converts words present in a list into uppercase
# and stores them in a set.

words = ["apple", "banana", "grape", "apple", "mango"]
uppercase_set = {word.upper() for word in words}

print("Original list:", words)
print("Uppercase set:", uppercase_set)
print(type(words))
print(type(uppercase_set))
