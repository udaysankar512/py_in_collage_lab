# Q.2. write a program to remove empty tuples from a list of tuple .

def remove_element(lst):
    result = []
    for tup in lst:
        if len(tup) == 0:
            continue
        else:
            result.append(tup)
    return result


list_of_tuples = [(), (1, 2), (), (3, 4, 5), (), (6,)]
print("Original list:", list_of_tuples)
print("After removing empty tuples:", remove_element(list_of_tuples))
