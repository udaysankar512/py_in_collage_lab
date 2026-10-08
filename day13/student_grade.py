# Q.1. Write a Python function to calculate a student's grade.
# The function accepts marks and returns the grade according to:
# 90 - 100 : A
# 80 - 89  : B
# 70 - 79  : C
# 60 - 69  : D
# Below 60 : F


def calculate_grade(marks):
    """Return the grade for the given marks."""
    if 90 <= marks <= 100:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    elif 0 <= marks < 60:
        return "F"
    else:
        raise ValueError("Marks must be between 0 and 100.")


marks = int(input("Enter your marks :"))
result = calculate_grade(marks)
print("Your Grade is : ",result)