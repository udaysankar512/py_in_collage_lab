#1. Write a recursive python function to flatten a deeply nested tuple of tuples into a single flat tuple containing all the individual values .

def flatten_tuple(t):
    result = ()

    for item in t:
        if isinstance(item, tuple):
            result += flatten_tuple(item)
        else:
            result += (item,)

    return result


nested = (1, (2, 3), ((4, 5), 6), (7, (8, 9)))

flat = flatten_tuple(nested)

print("Original tuple:", nested)
print("Flat tuple:", flat)