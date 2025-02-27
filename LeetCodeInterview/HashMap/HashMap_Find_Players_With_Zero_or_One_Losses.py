'''
 Find Players With Zero or One Losses
'''

'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player 
winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
'''
from collections import defaultdict
matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
winnerlooser = defaultdict(int)

winner=[]
looser=[]
for i in matches:
    winnerlooser[i[0]] += 0
    winnerlooser[i[1]] += 1

for value in winnerlooser:
    if winnerlooser[value]== 0:
        winner.append(value)
    if winnerlooser[value]== 1:
        looser.append(value)

ans= [sorted(winner),sorted(looser)]
print(ans)


''' this is time complexity O(n+k) basically sorting alghorithm is osedi in linear way '''

losses_count = [-1] * 100001

for winner, loser in matches:
    if losses_count[winner] == -1:
        losses_count[winner] = 0
    if losses_count[loser] == -1:
        losses_count[loser] = 1
    else:
        losses_count[loser] += 1

answer = [[], []]
for i in range(100001):
    if losses_count[i] == 0:
        answer[0].append(i)
    elif losses_count[i] == 1:
        answer[1].append(i)

print(answer)