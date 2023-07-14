#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.

'''
def longestConsecutive(nums):
    if nums==[]:
        return 0
    
    sortedNums=sorted(nums)
    counter=1
    maxLength=1
    print(sortedNums)

    for i in range(1,len(sortedNums)):
        prevVal=sortedNums[i-1]
        if sortedNums[i]==prevVal+1:
            counter+=1
        elif sortedNums[i]==prevVal:
            continue
        elif sortedNums[i]!=prevVal+1:
            if counter>maxLength:
                maxLength=counter
            counter=1
    if counter>maxLength:
        maxLength=counter
        
    return maxLength
'''
def longestConsecutive(nums):
    if nums==[]:
        return 0
    
    maxLength=1
    counter=1
    localCounter=1
    checkedNums={}

    numsSet=set(nums)
    for i in numsSet:
        if i not in checkedNums:
            while i+localCounter in numsSet:
                checkedNums[i+localCounter]=i+localCounter
                localCounter+=1
            counter=localCounter
            localCounter=1
            while i-localCounter in numsSet:
                checkedNums[i-localCounter]=i-localCounter
                localCounter+=1
            counter+=localCounter
            localCounter=1
            if counter>maxLength:
                maxLength=counter-1
        counter=1
        
    return maxLength


test=longestConsecutive([5,2,0,3,1,-1])
print(test)

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0

        sortedNums=sorted(nums)
        counter=1
        maxLength=1

        for i in range(1,len(sortedNums)):
            prevVal=sortedNums[i-1]
            if sortedNums[i]==prevVal+1:
                counter+=1
            elif sortedNums[i]==prevVal:
                continue
            elif sortedNums[i]!=prevVal+1:
                if counter>maxLength:
                    maxLength=counter
                counter=1
        if counter>maxLength:
            maxLength=counter
        
        return maxLength
'''