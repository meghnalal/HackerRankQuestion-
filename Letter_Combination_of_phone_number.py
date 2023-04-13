phone = {2: ['a', 'b', 'c'],
             3: ['d', 'e', 'f'],
             4: ['g', 'h', 'i'],
             5: ['j', 'k', 'l'],
             6: ['m', 'n', 'o'],
             7: ['p', 'q', 'r', 's'],
             8: ['t', 'u', 'v'],
             9: ['w', 'x', 'y', 'z']}

result=['']
string = '23'
'''brute force solution '''
for i in string: # 2,3
    num=int(i)
    temp = []
    for j in phone[num]: #
        for res in result:
            temp.append(res + j)
            print(temp)
    result = temp
print(result)

'''Recursive Function'''
'''Define a recursive function that takes a string of digits and a current string of letters as input.'''
'''If the input string is empty, append the current string to the result list and return.'''
'''Get the first digit from the input string.
For each letter corresponding to the digit, call the recursive function with the remaining 
string and the current string plus the letter.'''

'''Change the digits input to a string, since the input will only contain digits from 2-9 inclusive.

Define a recursive function that takes in the remaining digits as a string and returns all possible letter combinations.'''


def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []

    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        for char in phone[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result
