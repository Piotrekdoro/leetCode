'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode

Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]

Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''

def encode(strs):
    encodedStr=''
    
    for i in range(len(strs)):
        encodedStr=encodedStr+str(len(strs[i]))+'&'+str(strs[i])
    return encodedStr
        
def decode(strs):
    decodedStr=[]
    wordLength=''
    i=0
    
    while i!=len(strs):
        if strs[i].isdigit()==False:
            decodedStr.append(str(strs[i+1:i+1+int(wordLength)]))
            i+=int(wordLength)+1
            wordLength=''
        else:
            wordLength+=strs[i]
            i+=1
    return decodedStr


test=encode(['cat','dog'])
print(test)
testToo=decode(test)
print(testToo)

'''
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encodedStr=''
    
        for i in range(len(strs)):
            encodedStr=encodedStr+str(len(strs[i]))+'&'+str(strs[i])
        return encodedStr

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decodedStr=[]
        wordLength=''
        i=0
    
        while i!=len(strs):
            if strs[i].isdigit()==False:
                decodedStr.append(str(strs[i+1:i+1+int(wordLength)]))
                i+=int(wordLength)+1
                wordLength=''
            else:
                wordLength+=strs[i]
                i+=1
        return decodedStr
'''