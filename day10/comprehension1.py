# Q.1. Write a program to generate two lists using list comprehension.
# One list should contain the first 20 odd numbers and the other
# should contain the first 20 even numbers.

odd_numbers = [num for num in range(1, 41, 2)]
even_numbers = [num for num in range(2, 41, 2)]

print("First 20 odd numbers:", odd_numbers)
print("First 20 even numbers:", even_numbers)