# Q.3. write a program to creat folling 3 lists :
# --- a list of names.
# --- a list of roll names
# --- a list of marks
#    Generate and print a list of tuples contaning name, roll number and marks from the 3 lists. From this list generate 3 tuple 
#    --- one contaning all names 
#    --- another containing all roll numbers 
#    ----third containg all marks 


names = ["Uday", "Deba", "Nabayan"]
roll_numbers = [101, 102, 103]
marks = [85, 90, 78]

students = list(zip(names, roll_numbers, marks))
print("List of tuples (name, roll, marks):")
print(students)

persion1 = students[0]
persion2 = students[1]
persion3 = students[2]
print("persioon 1",persion1)
print("persioon 2",persion2)
print("persioon 3",persion3)

all_names, all_rolls, all_marks = zip(*students)
print("Tuple of all names:", all_names)
print("Tuple of all roll numbers:", all_rolls)
print("Tuple of all marks:", all_marks)