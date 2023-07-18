'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
'''
def generateParenthesis(n):
    res=[]
    
    if n==1:
        res.append('()')
        print(res)
    else:
        prevRes=generateParenthesis(n-1)
        resDict={}
        for i in range(len(prevRes)):
            if '('+prevRes[i]+')' not in resDict:
                res.append('('+prevRes[i]+')')
                resDict['('+prevRes[i]+')']=1
            if '()'+prevRes[i] not in resDict:
                res.append('()'+prevRes[i])
                resDict['()'+prevRes[i]]=1
            if prevRes[i]+'()' not in resDict:
                res.append(prevRes[i]+'()')
                resDict[prevRes[i]+'()']=1
            print(res)
    return res

test=generateParenthesis(3)
#print(test)

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
    
        if n==1:
            res.append('()')
            print(res)
        else:
            prevRes=generateParenthesis(n-1)
            resDict={}
            for i in range(len(prevRes)):
                if '('+prevRes[i]+')' not in resDict:
                    res.append('('+prevRes[i]+')')
                    resDict['('+prevRes[i]+')']=1
                if '()'+prevRes[i] not in resDict:
                    res.append('()'+prevRes[i])
                    resDict['()'+prevRes[i]]=1
                if prevRes[i]+'()' not in resDict:
                    res.append(prevRes[i]+'()')
                    resDict[prevRes[i]+'()']=1
                print(res)
        return res
'''