#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
        numsDict=dict()
        for i in range(len(nums)):
            if nums[i] in numsDict:
                return True
            else:
                numsDict[nums[i]]=i
        return False

'''
class Solution:
    def containsDuplicate(nums):
        numsDict=dict()
        for i in range(len(nums)):
            if nums[i] in numsDict:
                return True
            else:
                numsDict[nums[i]]=i
        return False
'''



nums=[1,2,3,1]