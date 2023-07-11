'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def twoSum(nums, target):
    numsRest={}
    for i in range(len(nums)):
        if nums[i] in numsRest:
            if i!=numsRest[nums[i]]:
                return([i, numsRest[nums[i]]])
        numsRest[target-nums[i]]=i
        
twoSum([5,7,8,7,10,3], 14)

'''
class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsRest={}
        for i in range(len(nums)):
            if nums[i] in numsRest:
                if i!=numsRest[nums[i]]:
                    return([i, numsRest[nums[i]]])
            numsRest[target-nums[i]]=i
'''