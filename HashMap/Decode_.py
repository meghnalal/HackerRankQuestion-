# Online Python compiler (interpreter) to run Python online.
key = "happy boy"
print(key)

#remove duplicates only if order doesnt matter
#print(set(key))
#print("".join(set(key)))

key = 'hello meghna'
result = "".join(dict.fromkeys(key))
words = result.split()
nospace = ''.join(words)
print(nospace)


import string

alphabeth = string.ascii_lowercase
print(alphabeth)

c= {}

for i in nospace:
    print(i)

i=0
mapping = {' ': ' '}
for char in nospace:
    if char not in mapping:
        mapping[char] = alphabeth[i]
        i += 1

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'

        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1

        for char in message:
            res += mapping[char]

        return res

    nospace = "your_input_string"
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Replace with your custom alphabet

    mapping = {char: alphabet[i] for i, char in enumerate(nospace) if char != ' '}