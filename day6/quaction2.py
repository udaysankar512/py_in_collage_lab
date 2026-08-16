#2. write a python program to modify a tuple by converting it to a list , changing a specific item ,and converting it back to a tuple.

my_tuple = (10, 20, 30, 40, 50)

print("Original tuple:", my_tuple)

# Convert tuple to list
my_list = list(my_tuple)

# Change the specific item
my_list[2] = 100

# Convert list back to tuple
my_tuple = tuple(my_list)

print("Modified tuple:", my_tuple)