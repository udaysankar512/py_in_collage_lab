# Q.2. Write a Python function that accepts a list and removes all negative numbers from it.


def remove_negative_numbers(numbers):
    """Return a new list without negative numbers."""
    return [num for num in numbers if num >= 0]



numbers = [12, -7, 0, -4, 9, -3, 15]
result = remove_negative_numbers(numbers)
print("Original list:", numbers)
print("List after removing negative numbers:", result)

