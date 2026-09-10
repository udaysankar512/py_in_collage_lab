# Q.2. Suppose a list contains 5 strings. Write a program to convert all
# strings to uppercase.

strings = ["apple", "banana", "grape", "mango", "orange"]
uppercase_strings = [word.upper() for word in strings]

print("Original list:", strings)
print("Uppercase list:", uppercase_strings)
