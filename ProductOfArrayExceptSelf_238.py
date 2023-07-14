#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):

    maxNum=1
    answer=[]

    for i in range(len(nums)):
        maxNum*=nums[i]
    print(maxNum)
    for i in range(len(nums)):
        print(maxNum*nums[i])
        answer.append(int(maxNum/nums[i]))
    return answer


test=productExceptSelf([1,2,3,4])
print(test)













#class Solution:
    #def productExceptSelf(self, nums: List[int]) -> List[int]: