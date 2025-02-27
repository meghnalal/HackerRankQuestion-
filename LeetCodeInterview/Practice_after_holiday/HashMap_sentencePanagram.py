'''

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
or false otherwise.

'''

sentence = "thequickbrownfoxjumpsoverthelazydog"

sentence_set = set(sentence)
alphabet_len = 26
if len(sentence_set) == alphabet_len:
    print(True)
