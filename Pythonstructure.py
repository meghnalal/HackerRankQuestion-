#integers, strings, and even functions can be stored within the same list.
'''
They represent the easiest way to store a collection of related objects.
They are easy to modify by removing, adding, and changing elements.
They are useful for creating nested data structures, such as a list of lists/dictionaries.
However, they also have cons:

They can be pretty slow when performing arithmetic operations on their elements. (For speed, use NumPy's arrays.)
They use more disk space because of their under-the-hood implementation.
'''

# Create an empty list using square brackets
l1 = []

# Create a four-element list using square brackets
l2 = [1, 2, "3", 4]  # Note that this lists contains two different data types: integers and strings

# Create an empty list using the list() constructor
l3 = list()

# Create a three-element list from a tuple using the list() constructor
# We will talk about tuples later in the tutorial
l4 = list((1, 2, 3))

# Print out lists
print(f"List l1: {l1}")
print(f"List l2: {l2}")
print(f"List l3: {l3}")
print(f"List l4: {l4}")


l2 = ["0", "Ready", "Not"]
signal = ["0","Ready","Not","Ready","0","Not"]

l2 = ["0", "Ready", "Not"]
signal = ["0", "Ready", "Not", "Ready", "0", "Not"]

def detect_rising_falling_edges(signal_list):
    prev_signal = None
    edge_indices = []
    for i, current_signal in enumerate(signal_list):
        if prev_signal is not None:
            if prev_signal == "0" and current_signal == "Ready":
                edge_indices.append(i - 1)  # Index of the "0" element
            elif prev_signal == "Ready" and current_signal == "Not":
                edge_indices.append(i - 1)  # Index of the "Ready" element
        prev_signal = current_signal
    return edge_indices

# Call the function with the 'signal' list to get the edge indices
edge_indices = detect_rising_falling_edges(signal)
print("Rising/Falling Edge Indices:", edge_indices)

import pandas as pd

l2 = ["0", "Ready", "Not"]
signal_list = ["0", "Ready", "Not", "Ready", "0", "Not"]

# Convert the signal_list to a pandas Series
signal_series = pd.Series(signal_list)


def detect_rising_falling_edges(signal_series):
    prev_signal = None
    rising_edge_indices = []
    falling_edge_indices = []

    for i, current_signal in signal_series.items():
        if prev_signal is not None:
            if prev_signal == "0" and current_signal == "Ready":
                rising_edge_indices.append(i - 1)  # Index of the "0" element
            elif prev_signal == "Ready" and current_signal == "Not":
                falling_edge_indices.append(i - 1)  # Index of the "Ready" element
        prev_signal = current_signal

    return rising_edge_indices, falling_edge_indices


# Call the function with the 'signal_series' to get the rising and falling edge indices
rising_edge_indices, falling_edge_indices = detect_rising_falling_edges(signal_series)

print("Rising Edge Indices:", rising_edge_indices)
print("Falling Edge Indices:", falling_edge_indices)


import pandas as pd

# Sample data with more than 10 unique values
data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

# Convert the data to a pandas Series and then convert it to Categorical
categorical_series = pd.Series(data, dtype="category")

# Access the Categorical representation using `series.cat`
categorical_enum = categorical_series.cat.codes

print(categorical_enum)