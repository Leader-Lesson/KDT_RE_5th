# Tuple Example

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Slice from index 1 to 3:", my_tuple[1:4])

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Nested tuples
nested_tuple = (my_tuple, (6, 7, 8))
print("Nested tuple:", nested_tuple)

# Length of a tuple
print("Length of my_tuple:", len(my_tuple))

# Checking membership
print("Is 3 in my_tuple?", 3 in my_tuple)
print("Is 10 in my_tuple?", 10 in my_tuple)

# Concatenating tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", new_tuple)

# Repeating tuples
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)