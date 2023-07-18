'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

EXAMPLE
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9  

************************************************
'''

def evalRPN(tokens):

    i=0
    res=0
    operandsDict={'+':lambda a,b:a+b,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:a/b,}

    while tokens!=[]:
        if tokens[i] in operandsDict:
            print(tokens)
            res=operandsDict[tokens[i]](int(tokens[i-2]),int(tokens[i-1]))
            tokens[i]=res
            del tokens[i-1]
            del tokens[i-2]
            i-=2
            if len(tokens)==1:
                return int(tokens[0])
        i+=1
    


#test=evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) #22
test=evalRPN(['10','6',"9","3","+",'-11','*','/','*','17','+','5','+']) #22
print(test)

'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i=0
        res=0
        operandsDict={'+':lambda a,b:a+b,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:a/b,}
    

        while tokens!=[]:
            if tokens[i] in operandsDict:
                res=operandsDict[tokens[i]](int(tokens[i-2]),int(tokens[i-1]))
                tokens[i]=res
                del tokens[i-1]
                del tokens[i-2]
                i-=2
                if len(tokens)==1:
                    return int(tokens[0])
            i+=1
'''














