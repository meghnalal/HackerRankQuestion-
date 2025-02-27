'''
Check if the Sentence Is Pangram
'''
'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, 

or false otherwise.


Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

'''

sentence = "leetcode"

alphabeth= set("abcdefghijklmnopqrstuvwxyz")

for i in alphabeth:
    if i not in sentence:
        print(False)
        break
print(True)

''' better solution as set doenast repeat caractehrs '''
print( len(set(sentence))==26)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabeth= set("abcdefghijklmnopqrstuvwxyz")
        for i in alphabeth:
            if i not in sentence:
                return(False)
                break
        return(True)

''' if this was a dict also cant have repeated keys '''

sentence = "leetcode"
letter_count = {}

for letter in sentence:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)