'''recursive function of factorial with
{ n * (n-1) if n>=0
{ 1         if n=0 because (0-1)would break the code
'''
def dfs(n):
    if n >= 1 :
        return n * dfs(n-1)
    else:
        return 1
print(dfs(2))


'''recusion not needed'''
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
         return_value *= i
    return return_value

print(factorial(4))


setup_string = '''def dfs(n):
    if n >= 1 :
        return n * dfs(n-1)
    else:
        return 1
print(dfs(2))'''

from timeit import timeit
timeit("dfs(4)", setup=setup_string, number=10000000)


setup_string = '''def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
         return_value *= i
    return return_value'''

from timeit import timeit
timeit("factorial(4)", setup=setup_string, number=10000000)
