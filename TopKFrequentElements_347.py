'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
''''''
def topKFrequent(nums, k):
    numsDict={}
    kMostFreq=[]

    for i in range(len(nums)):
        if nums[i] in numsDict:
            numsDict[nums[i]]+=1
        else:
            numsDict[nums[i]]=1
    print(numsDict)
    numsSorted=sorted(numsDict.items(),key=lambda numTouple:numTouple[1],reverse=True)
    print(numsSorted)
    for i in range(k):
        kMostFreq.append(numsSorted[i][0])
    return kMostFreq

print(topKFrequent([-1,-1],1))
print(topKFrequent([1,1,1,2,2,3],2))

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict={}
        kMostFreq=[]

        for i in range(len(nums)):
            if nums[i] in numsDict:
                numsDict[nums[i]]+=1
            else:
                numsDict[nums[i]]=1
        print(numsDict)
        numsSorted=sorted(numsDict.items(),key=lambda numTouple:numTouple[1],reverse=True)
        print(numsSorted)
        for i in range(k):
            kMostFreq.append(numsSorted[i][0])
        return kMostFreq
'''


