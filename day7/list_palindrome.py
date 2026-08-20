
def is_palindrome(lst):
    return lst == lst[::-1] 


my_list = [1, 2, 3, 2, 1]

if is_palindrome(my_list):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
