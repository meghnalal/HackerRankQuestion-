'''
Find Players With Zero or One Losses
'''

'''
You are given an integer array matches where matches[i] = [winneri, loseri]
indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.
'''
from collections import defaultdict


matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

counts = defaultdict(int)

winner1 = []
losers1 = []

for winner, losses in matches:
    counts[winner] += 0
    counts[losses] += 1

for key, value in counts.items():
    if value ==  0 :
        winner1.append(key)
    if value ==  1 :
        losers1.append(key)

print([sorted(winner1),sorted(losers1)])

