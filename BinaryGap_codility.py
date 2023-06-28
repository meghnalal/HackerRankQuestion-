
def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num // 2)
            print (num % 2)
DecimalToBinary(6)

def decimalToBinary(n):
    return "{0:b}".format(int(n))

decimalToBinary(6)


x="{0:b}".format(int(70))

def solution(N):
    binary_str = "{0:b}".format(N)
    max_gap = 0
    current_gap = 0
    for bit in binary_str:
        if bit == '1':
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        else:
            current_gap += 1
    return max_gap
print(solution(534))


'''Meghna doing it'''
def gap(N):
    binary_str = "{0:b}".format(N)
    maxgap=0
    currentgap=0
    for i in binary_str:
        if i > '0':
            if currentgap>maxgap:
                maxgap=currentgap
        else:
            currentgap=currentgap+1
    return maxgap

print(gap(300))