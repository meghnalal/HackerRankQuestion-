'''
791. Custom Sort String
'''

'''

791. Custom Sort String
'''
from collections import defaultdict
order = "kqep"
s = "pekeq"

# "kqeep"


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
