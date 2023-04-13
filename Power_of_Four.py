import math
n = 17
if n <= 0:
    print('False')
x=math.log(n,4)
if x==int(x):
    print('True')
else:
    print('False')

'''recursivly'''


def is_power_of_four(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return is_power_of_four(n // 4)
