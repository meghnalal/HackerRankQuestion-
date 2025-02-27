'''
2000. Reverse Prefix of Word
'''

'''
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 
and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, 
do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends 
at 3 (inclusive). The resulting string will be "dcbaefd".

'''
word = "abcdefd"
ch = "d"
word_list = list(word)

word = list(word)
try:
    index = word.index(ch)
except:
    print("".join(word))
index=0

# for i in range(len(word)):
#     if word[i] == ch:
#         index = i
#         break

left=0
right = index

while left < right :
    word_list[left], word_list[right] =  word_list[right], word_list[left]
    left += 1
    right -= 1


