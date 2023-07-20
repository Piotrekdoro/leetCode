'''
A phrase is a palindrome if, after converting all uppercase letters into lower letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, string):
        frontPointer=0
        backPointer=len(string)-1
        
        if len(string)==0:
            return True
        #if len(string)==1:
        #    if string.isalnum()==True:
        #        return True
        #    else:
        #        return False

        while frontPointer<backPointer:
        
            while string[frontPointer].isalnum()==False:
                #print('Frontpointer is: '+str(frontPointer))
                frontPointer+=1
                if frontPointer==backPointer and backPointer==len(string)-1:
                    return True
                #print('Frontpointer moved to: '+str(frontPointer))
            while string[backPointer].isalnum()==False:
                #print('Backpointer moved to: '+str(backPointer))
                backPointer-=1
                #print('Backpointer moved to: '+str(backPointer))

            if string[frontPointer].lower()!=string[backPointer].lower():
                return False
            frontPointer+=1
            backPointer-=1
            #print('Frontpointer moved in outer loop to: '+str(frontPointer))
            #print('Backpointer moved in outer loop to: '+str(backPointer))
        return True



test=Solution()
print(test.isPalindrome('A'))