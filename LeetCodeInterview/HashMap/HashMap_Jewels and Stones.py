'''
Jewels and Stones
'''

'''
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have.
 You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

from collections import defaultdict
jewels = "aA"
stones = "aAAbbbb"

stonedict = defaultdict(int)

for i in stones:
    stonedict[i] += 1
ans=0
for z in jewels:
    if z in stonedict:
        ans += stonedict[z]
print(ans)
