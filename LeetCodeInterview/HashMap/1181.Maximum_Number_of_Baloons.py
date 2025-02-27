'''
1189. Maximum Number of Balloons
'''

'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

'''

from collections import defaultdict
text = "llbb"
balloon= 'balloon'
# balloon1=set(balloon)
# dictionary = defaultdict(int)
#
# for texts in text:
#     if texts in balloon1:
#         dictionary[texts] += 1
# print(dictionary)
#
# dictionary['b'] = dictionary['b']
# dictionary['a'] = dictionary['a']
# dictionary['n'] = dictionary['n']
# dictionary['l'] = dictionary['l'] // 2
# dictionary['o'] = dictionary['o']//2
#
# minval = min(dictionary.values())
# print(minval)


from collections import Counter
'''better solution'''

pattern = "balloon"
dictOfPattern = defaultdict(int)
dictOfText = defaultdict(int)
ans = float("inf")

dictOfPattern = Counter(pattern)
dictOfText = Counter(text)

for key in dictOfPattern:
    ans = min(ans, dictOfText[key] // dictOfPattern[key])

print ((ans))