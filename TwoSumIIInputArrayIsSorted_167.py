'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they
add up to a specific numbers number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
'''
class Solution:
    def twoSum(self, numbers, target):
        frontPointer,backPointer=0,len(numbers)-1
        print('frontPointer is initially: '+str(frontPointer))
        print('backPointer is initially: '+str(backPointer))
        while frontPointer<backPointer:
            if numbers[frontPointer]+numbers[backPointer]>target:
                print('Moved backPointer to: '+str(backPointer))
                backPointer-=1
            elif numbers[frontPointer]+numbers[backPointer]<target:
                print('Moved frontPointer to: '+str(frontPointer))
                frontPointer+=1
            elif numbers[frontPointer]+numbers[backPointer]==target:
                print('Done, frontPointer: '+str(frontPointer))
                print('Done, backPointer: '+str(backPointer))
                return [frontPointer+1,backPointer+1]
                


test=Solution()
print(test.twoSum([2,5,7,11,15],16))