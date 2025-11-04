# Dictionary in Python

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)

# Updating an existing value
my_dict["age"] = 31
print(my_dict)

# Removing a key-value pair
del my_dict["city"]
print(my_dict)

# Looping through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary.")

# Getting the keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)
print(values)