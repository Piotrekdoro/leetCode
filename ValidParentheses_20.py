'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
'''
#class Solution:
#    def isValid(self, strs: str) -> bool:

def isValid(strs):
    bracketStack=[]

    for i in range(len(strs)):
        if strs[i]=='(':
            bracketStack.append('()')
        elif strs[i]=='[':
            bracketStack.append('[]')
        elif strs[i]=='{':
            bracketStack.append('{}')
        if (strs[i]==')' or strs[i]==']' or strs[i]=='}') and (bracketStack==[]):
            return False
        if strs[i]==')' and bracketStack[len(bracketStack)-1]!='()':
            return False
        elif strs[i]==')' and bracketStack[len(bracketStack)-1]=='()':
            bracketStack.pop()
        if strs[i]==']' and bracketStack[len(bracketStack)-1]!='[]':
            return False
        elif strs[i]==']' and bracketStack[len(bracketStack)-1]=='[]':
            bracketStack.pop()
        if strs[i]=='}' and bracketStack[len(bracketStack)-1]!='{}':
            return False
        elif strs[i]=='}' and bracketStack[len(bracketStack)-1]=='{}':
            bracketStack.pop()
        print(bracketStack)

    if bracketStack==[]:
        return True
    else:
        return False

test=isValid('(){}}{')
print(test)