'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums):
        sorted(nums)
        frontPointer,backPointer=0,len(nums)-1
        newNums=nums[:frontPointer]+nums[frontPointer+1:backPointer]+nums[backPointer+1:]
        print(nums)
        print(newNums)
        target=-nums[frontPointer]-nums[backPointer]

        while frontPointer<backPointer:

            if newNums[frontPointer]+newNums[backPointer]>target:
                backPointer-=1
            elif nums[frontPointer]+nums[backPointer]<target:
                frontPointer+=1
            elif nums[frontPointer]+nums[backPointer]==target:
                return [frontPointer+1,backPointer+1]
          


test=Solution()
print(test.threeSum([2,5,7,11,15]))