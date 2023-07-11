#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



def isAnagram(s, t):
        if len(s)!=len(t):
            return False
        else:
              sSorted=sorted(list(s))
              tSorted=sorted(list(t))
              return sSorted==tSorted
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
              sSorted=sorted(list(s))
              tSorted=sorted(list(t))
              return sSorted==tSorted
'''

print(isAnagram('cat', 'tac'))