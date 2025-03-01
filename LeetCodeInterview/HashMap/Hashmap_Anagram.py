'''
Group Anagram
'''

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

how to sort 
sorted(string)
'''
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
group_dictionary = defaultdict(list)

for i in strs:
    sorted_i = ''.join(sorted(i))
    group_dictionary[sorted_i].append(i)
print(group_dictionary.values())