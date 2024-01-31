'''
A hash table, also known as a hash map, is a data structure in Python
and many other programming languages that allows you to store and
retrieve values based on keys.
It's an efficient way to associate values with keys,
making it quick to look up and access data.

'''

# Creating a hash table (dictionary)
my_dict = {}

# Storing data
my_dict["name"] = "Alice"
my_dict["age"] = 30
my_dict["city"] = "New York"

# Retrieving data
print(my_dict["name"])  # Output: "Alice"
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: "New York"

'''can have a list in the key if i want to'''

my_dict["name"] = ["Alice", "Rex"]
print(my_dict["name"])       # Output: ["Alice", "Rex"]
print(my_dict["name"][0])    # Output: "Alice"
print(my_dict["name"][1])    # Output: "Rex"

# Adding another name to the list
my_dict["name"].append("Charlie")
print(my_dict["name"])       # Output: ["Alice", "Rex", "Charlie"]