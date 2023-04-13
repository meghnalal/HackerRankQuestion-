a=2
b=3

while b != 0:
        # Calculate the carry
        carry = a & b

        # Calculate the sum
        a = a ^ b

        # Shift the carry by one bit to the left
        #b = carry << 1

    #print( a )

''' actual solution  not finished i dont understand why '''
#def add(a: int, b: int) -> int:
    # Iterate until there is no carry
def add(a: int, b: int) -> int:
    # Iterate until there is no carry
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Calculate the sum
        a = a ^ b

        # Shift the carry by one bit to the left
        b = carry << 1

    return a
