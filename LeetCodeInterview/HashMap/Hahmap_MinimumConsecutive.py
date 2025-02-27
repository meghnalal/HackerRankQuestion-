'''
Example 2: 2260. Minimum Consecutive Cards to Pick Up
'''
'''
Given an integer array cards, find the length of the shortest subarray 
that contains at least one duplicate. If the array has no duplicates, return -1.

'''
from collections import defaultdict
# my sollution was better
cards = [1,0,5,3]
card_dictionary = defaultdict(int) 
ans = float("inf")

for i in range(len(cards)):
    if cards[i] in card_dictionary:
        ans= min(ans,i+1 - card_dictionary[cards[i]])
    card_dictionary[cards[i]] = i

print( -1 if ans == float("inf") else ans)


# solution does the same thing however its just  saiing each pair
cards = [3,4,2,3,4,7]
dic = defaultdict(list)
for i in range(len(cards)):
    dic[cards[i]].append(i)

ans = float("inf")
for key in dic:
    arr = dic[key]
    for i in range(len(arr) - 1):
        ans = min(ans, arr[i + 1] - arr[i] + 1)
