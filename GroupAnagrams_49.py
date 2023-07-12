'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

def groupAnagrams(strs): 
    anagramDict={}
    wordDict={}     
    for i in range(len(strs)):
        for j in range(len(strs[i])):   
            if bool(strs[i][j] in wordDict)==False:
                wordDict[strs[i][j]]=1
            else:
                wordDict[strs[i][j]]+=1
        if bool(frozenset(wordDict.items()) in anagramDict)==False:
            anagramDict[frozenset(wordDict.items())]=[]
            anagramDict[frozenset(wordDict.items())].append(strs[i])
        else:
            anagramDict[frozenset(wordDict.items())].append(strs[i])
        wordDict={}
    print(anagramDict)

    anagramList=[None]*len(anagramDict.keys())
    print(anagramList)
    counter=0 
    for item in anagramDict.items():
        print(item)
        anagramList[counter]=item[1]
        counter+=1
    print(anagramList)
    
    return(anagramList)

groupAnagrams(["eat","tea","tan","ate","nat","bat"])

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict={}
        wordDict={}     
        for i in range(len(strs)):
            for j in range(len(strs[i])):   
                if bool(strs[i][j] in wordDict)==False:
                    wordDict[strs[i][j]]=1
                else:
                    wordDict[strs[i][j]]+=1
            if bool(frozenset(wordDict.items()) in anagramDict)==False:
                anagramDict[frozenset(wordDict.items())]=[]
                anagramDict[frozenset(wordDict.items())].append(strs[i])
            else:
                anagramDict[frozenset(wordDict.items())].append(strs[i])
            wordDict={}

        anagramList=[None]*len(anagramDict.keys())
        counter=0 
        for item in anagramDict.items():
            anagramList[counter]=item[1]
            counter+=1
    
        return(anagramList)

    #groupAnagrams(["eat","tea","tan","ate","nat","bat"])
'''

