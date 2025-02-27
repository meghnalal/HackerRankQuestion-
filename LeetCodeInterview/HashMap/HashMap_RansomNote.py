'''
Ransom Note
'''

'''
Given two strings ransomNote and magazine, return true if 
ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "aa", magazine = "ab"
Output: false
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
from collections import defaultdict

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

dictMagazine= defaultdict(int)
dictRansom= defaultdict(int)

for i in magazine:
    dictMagazine[i] += 1

ans = True

for j in ransomNote:
    if j not in dictMagazine:
        ans = False
        break
    if j in dictMagazine:
        dictMagazine[j] -= 1
        if dictMagazine[j] < 0:
            ans = False
            break
print(ans)


# with 2  dictionary method 

ransomNote = "a"
magazine = "b"

dictMagazine= defaultdict(int)
dictRansom= defaultdict(int)

for i in magazine:
    dictMagazine[i] += 1

for j in ransomNote:
    dictRansom[j] += 1

for i in dictRansom:
    if i  not in dictMagazine:
        print(False)
        break
    if dictMagazine[i] < dictRansom[i]:
        print(False)
        break

