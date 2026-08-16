# 4. write a python program to sort a tuple of based on the second item in each nested tuple .

students = (
    ("Alice", 80),
    ("Bob", 60),
    ("John", 90),
    ("David", 70)
)

sorted_students = tuple(sorted(students, key=lambda x: x[1]))

print("Original tuple:", students)
print("Sorted tuple:", sorted_students)