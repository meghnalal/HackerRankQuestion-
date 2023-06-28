names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]
'''see the len will not give actual len of this wich is 10 as it has sub section'''
print(len(names))

'''Traverse a Nested List Recursively fit this problem '''
def dfs(names):
    count = 0
    for name in names:
        if isinstance(name,list):
            count=count + dfs(name)
        else:
            count=count + 1
    return count

def print_names(names):
    for name in names:
        if isinstance(name, list):
            print_names(name)
        elif name is not None:
            print(name)

print(dfs(names))
print(print_names(names))

