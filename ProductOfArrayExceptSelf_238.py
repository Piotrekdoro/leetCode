#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):

    curVal=1
    answer=[]
    multiplyForward=[]
    multiplyBackward=[]

    for i in range(len(nums)):
        curVal*=nums[i]
        multiplyForward.append(curVal)
    curVal=1
    for i in reversed(range(len(nums))):
        curVal*=nums[i]
        multiplyBackward.append(curVal)
    multiplyBackward.reverse()
    answer.append(multiplyBackward[1])
    for i in range(1,len(nums)-1):
        answer.append(multiplyForward[i-1]*multiplyBackward[i+1])
    answer.append(multiplyForward[len(nums)-2])
    return answer

test=productExceptSelf([1,2,3,4])
print(test)












'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curVal=1
        answer=[]
        multiplyForward=[]
        multiplyBackward=[]

        for i in range(len(nums)):
            curVal*=nums[i]
            multiplyForward.append(curVal)
        curVal=1
        for i in reversed(range(len(nums))):
            curVal*=nums[i]
            multiplyBackward.append(curVal)
        multiplyBackward.reverse()
        answer.append(multiplyBackward[1])
        for i in range(1,len(nums)-1):
            answer.append(multiplyForward[i-1]*multiplyBackward[i+1])
        answer.append(multiplyForward[len(nums)-2])
        return answer
'''