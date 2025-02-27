'''
791. Custom Sort String
'''

'''
You are given two strings order and s. All the characters of order are 
unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, 
then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
'''
from collections import defaultdict

# order = "cba"
# s = "abcd"
order = "bcafg"
s = "abcd"

setorder=defaultdict(int)
stes= defaultdict(int)
ans=[]
for x in order:
    setorder[x] +=1

for y in s:
    stes[y] +=1

for i in setorder:
    if i in stes:
        ans.append(i*stes[i])
for c in stes:
    if c not in setorder:
        ans.append(c*stes[c])

#  trying again without looking
from collections import defaultdict
order = "bcafg"
s = "abcd"
dictorder=defaultdict(int)
dicts=defaultdict(int)

for i in order:
    dictorder[i] += 1

for v in order:
    dicts[v] += 1
result=[]
for x in dictorder:
    if x in dicts:
        result.append(x * dicts[x])

for y in dicts:
    if y not in dictorder:
        result.append(y * dicts[y])
