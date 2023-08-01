'''
Given a string s, find the length of the longest substring without repeating characters.
'''
#Optimized for speed
class Solution:
    def lengthOfLongestSubstring(self, s):
        letters={}
        length=0
        maxLength=0
        start=0
        window=[]

        i=0
        while i<len(s):
            if s[i] not in letters:
                letters[s[i]]=i
                length+=1
                i+=1
            else:
                if length>maxLength:
                    maxLength=length
                
                length=i-letters[s[i]]-1
                window=s[start:letters[s[i]]+1]
                start=letters[s[i]]+1
                
                for item in window:
                    del letters[item]
                        
        if length>maxLength:
            maxLength=length

        return maxLength


test=Solution().lengthOfLongestSubstring('abcabcbb')
print(test)

'''
#Optimized for memory
class Solution:
    def lengthOfLongestSubstring(self, s):
        letters={}
        length=0
        maxLength=0

        #if len(s)==1:
        #    return 1

        i=0
        while i<len(s):
            if s[i] not in letters:
                letters[s[i]]=i
                length+=1
                i+=1
            else:
                if length>maxLength:
                    maxLength=length
                i=letters[s[i]]+1
                length=0
                letters={}
        
        if length>maxLength:
            maxLength=length

        return maxLength
'''