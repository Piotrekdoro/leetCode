'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
''''''
def topKFrequent(nums, k):
    numsDict={}
    kBiggestNums=[]

    for i in range(len(nums)):
        print('loop: '+str(i))
        #print(kBiggestNums.count(nums[i]))
        #print(bool(len(kBiggestNums)<k))
        #print(bool(kBiggestNums.count(nums[i])!=0))
        if kBiggestNums==[]:
            kBiggestNums.append(nums[i])
            numsDict[nums[i]]=1
            print(nums[i])
            print(numsDict)
            print(kBiggestNums)
        elif len(kBiggestNums)<k and kBiggestNums.count(nums[i])==0:
            kBiggestNums.append(nums[i])
            numsDict[nums[i]]=1
            print(nums[i])
            print(numsDict)
            print(kBiggestNums)
        elif len(kBiggestNums)<k and kBiggestNums.count(nums[i])!=0:
            numsDict[nums[i]]+=1
            print(nums[i])
            print(numsDict)
            print(kBiggestNums)
        elif len(kBiggestNums)==k:
            kBiggestNums.sort()
            if nums[i]>kBiggestNums[0] and kBiggestNums.count(nums[i])==0:
                del numsDict[kBiggestNums[0]]
                kBiggestNums.pop(0)
                kBiggestNums.append(nums[i])
                numsDict[nums[i]]=1
                print(nums[i])
                print(numsDict)
                print(kBiggestNums)
            elif nums[i]>=kBiggestNums[0] and kBiggestNums.count(nums[i])!=0:
                numsDict[nums[i]]+=1
                print(nums[i])
                print(numsDict)
                print(kBiggestNums)
    return kBiggestNums

topKFrequent([2,5,2,2,3,4,3,8,5],3)

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict={}
        kBiggestNums=[]

        for i in range(len(nums)):
            if kBiggestNums==[]:
                kBiggestNums.append(nums[i])
                numsDict[nums[i]]=1
            elif len(kBiggestNums)<k and kBiggestNums.count(nums[i])==0:
                kBiggestNums.append(nums[i])
                numsDict[nums[i]]=1
            elif len(kBiggestNums)<k and kBiggestNums.count(nums[i])!=0:
                numsDict[nums[i]]+=1
            elif len(kBiggestNums)==k:
                kBiggestNums.sort()
                if nums[i]>kBiggestNums[0] and kBiggestNums.count(nums[i])==0:
                    del numsDict[kBiggestNums[0]]
                    kBiggestNums.pop(0)
                    kBiggestNums.append(nums[i])
                    numsDict[nums[i]]=1
                elif nums[i]>=kBiggestNums[0] and kBiggestNums.count(nums[i])!=0:
                    numsDict[nums[i]]+=1
'''