'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums):
        sortedNums=sorted(nums)
        results=[]
        resultsDict={}

        while len(sortedNums)>2:
            target=-sortedNums[0]
            frontPointer=1
            backPointer=(len(sortedNums)-1)
            
            
            while frontPointer<backPointer:
                twoSum=sortedNums[frontPointer]+sortedNums[backPointer]
                
                if twoSum==target:
                    singleResult=tuple(sorted([-target,sortedNums[frontPointer],sortedNums[backPointer]]))
                    resultsDict[singleResult]=resultsDict.get(singleResult,0)+1
                    if resultsDict[singleResult]==1:
                        results.append(list(singleResult))
                    frontPointer+=1
                    backPointer-=1
                elif twoSum<target:
                    frontPointer+=1
                else:
                    backPointer-=1
            
            while len(sortedNums)>1 and sortedNums[0]==sortedNums[1]:
                del sortedNums[1]
            del sortedNums[0]

        return results

#test=Solution().threeSum([-1,0,1,2,-1,-4])
#test=Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]) #[[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
test=Solution().threeSum([-2,0,1,1,2])#[[-2,0,2],[-2,1,1]]

print(test)


'''
#works bur slow


class Solution:
    def threeSum(self, nums):
        sortedNums=sorted(nums)
        results=[]
        resultsDict={}

        while len(sortedNums)>2:
            target=-sortedNums[0]
            frontPointer=1
            backPointer=(len(sortedNums)-1)
            
            
            while frontPointer<backPointer:
                twoSum=sortedNums[frontPointer]+sortedNums[backPointer]
                
                if twoSum==target:
                    singleResult=tuple(sorted([-target,sortedNums[frontPointer],sortedNums[backPointer]]))
                    #print(singleResult)
                    resultsDict[singleResult]=resultsDict.get(singleResult,0)+1
                    if resultsDict[singleResult]==1:
                        results.append(list(singleResult))
                    frontPointer+=1
                    backPointer-=1
                elif twoSum<target:
                    frontPointer+=1
                else:
                    backPointer-=1
            
            del sortedNums[0]

        #print(resultsDict)
        #print(results)
        return results
    '''

'''
#better, implemented deleting duplicate targets
class Solution:
    def threeSum(self, nums):
        sortedNums=sorted(nums)
        results=[]
        resultsDict={}

        while len(sortedNums)>2:
            target=-sortedNums[0]
            frontPointer=1
            backPointer=(len(sortedNums)-1)
            
            
            while frontPointer<backPointer:
                twoSum=sortedNums[frontPointer]+sortedNums[backPointer]
                
                if twoSum==target:
                    singleResult=tuple(sorted([-target,sortedNums[frontPointer],sortedNums[backPointer]]))
                    resultsDict[singleResult]=resultsDict.get(singleResult,0)+1
                    if resultsDict[singleResult]==1:
                        results.append(list(singleResult))
                    frontPointer+=1
                    backPointer-=1
                elif twoSum<target:
                    frontPointer+=1
                else:
                    backPointer-=1
            
            while len(sortedNums)>1 and sortedNums[0]==sortedNums[1]:
                del sortedNums[1]
            del sortedNums[0]

        return results'''

'''
#Implemented duplicates when solution is found
class Solution:
    def threeSum(self, nums):
        sortedNums=sorted(nums)
        results=[]
        resultsDict={}

        while len(sortedNums)>2:
            target=-sortedNums[0]
            frontPointer=1
            backPointer=(len(sortedNums)-1)
            print('*************************************')
            print('Current sortesNums: '+str(sortedNums))
            print('Current target: '+str(target))
            print('Back and front pointers reset')
            

            while frontPointer<backPointer:
                twoSum=sortedNums[frontPointer]+sortedNums[backPointer]
                print('-------------------------------------------')
                print('TwoSum: '+str(twoSum))
                print('Analized range: '+str(sortedNums[frontPointer:backPointer+1]))

                if twoSum==target:
                    singleResult=tuple(sorted([-target,sortedNums[frontPointer],sortedNums[backPointer]]))
                    print('Detected results: '+str(singleResult))
                    resultsDict[singleResult]=resultsDict.get(singleResult,0)+1
                    if resultsDict[singleResult]==1:
                        results.append(list(singleResult))
                        print('Results without duplicates: '+str(results))
                    while frontPointer+1!=len(sortedNums)-1 and sortedNums[frontPointer]==sortedNums[frontPointer+1]:
                        frontPointer+=1
                        print('moved frontpointer in while: '+str(frontPointer))
                    frontPointer+=1
                    print('moved frontpointer outside while: '+str(frontPointer))
                    while backPointer-1!=0 and sortedNums[backPointer-1]==sortedNums[backPointer]:
                        backPointer-=1
                        print('moved backpointer in while: '+str(backPointer))
                    backPointer-=1
                    print('moved backpointer in while: '+str(backPointer))
                elif twoSum<target:
                    frontPointer+=1
                    print('moved frontpointer in twoSum<target: '+str(frontPointer))
                else:
                    backPointer-=1
                    print('moved backpointer in twoSum>target: '+str(backPointer))
                print('Analized range: '+str(sortedNums[frontPointer:backPointer+1]))
                testing=[0,1]

            while len(sortedNums)>1 and sortedNums[0]==sortedNums[1]:
                del sortedNums[1]
            del sortedNums[0]

        return results
'''

'''
#Implemented duplicates if there isnt a solution

class Solution:
    def threeSum(self, nums):
        sortedNums=sorted(nums)
        results=[]
        resultsDict={}

        while len(sortedNums)>2:
            target=-sortedNums[0]
            frontPointer=1
            backPointer=(len(sortedNums)-1)
            print('*************************************')
            print('Current sortesNums: '+str(sortedNums))
            print('Current target: '+str(target))
            print('Back and front pointers reset')
            

            while frontPointer<backPointer:
                twoSum=sortedNums[frontPointer]+sortedNums[backPointer]
                print('-------------------------------------------')
                print('TwoSum: '+str(twoSum))
                print('Analized range: '+str(sortedNums[frontPointer:backPointer+1]))

                if twoSum==target:
                    singleResult=tuple(sorted([-target,sortedNums[frontPointer],sortedNums[backPointer]]))
                    print('Detected results: '+str(singleResult))
                    resultsDict[singleResult]=resultsDict.get(singleResult,0)+1
                    if resultsDict[singleResult]==1:
                        results.append(list(singleResult))
                        print('Results without duplicates: '+str(results))
                    while frontPointer+1!=len(sortedNums)-1 and sortedNums[frontPointer]==sortedNums[frontPointer+1]:
                        frontPointer+=1
                        print('moved frontpointer in while: '+str(frontPointer))
                    frontPointer+=1
                    print('moved frontpointer outside while: '+str(frontPointer))
                    while backPointer-1!=0 and sortedNums[backPointer-1]==sortedNums[backPointer]:
                        backPointer-=1
                        print('moved backpointer in while: '+str(backPointer))
                    backPointer-=1
                    print('moved backpointer in while: '+str(backPointer))
                elif twoSum<target:
                    while frontPointer+1!=len(sortedNums)-1 and sortedNums[frontPointer]==sortedNums[frontPointer+1]:
                        frontPointer+=1
                    frontPointer+=1
                    print('moved frontpointer in twoSum<target: '+str(frontPointer))
                else:
                    while backPointer-1!=0 and sortedNums[backPointer-1]==sortedNums[backPointer]:
                        backPointer-=1
                    backPointer-=1
                    print('moved backpointer in twoSum>target: '+str(backPointer))
                print('Analized range: '+str(sortedNums[frontPointer:backPointer+1]))
                testing=[0,1]

            while len(sortedNums)>1 and sortedNums[0]==sortedNums[1]:
                del sortedNums[1]
            del sortedNums[0]

        return results
'''

'''
#taken result duplicats checking out
class Solution:
    def threeSum(self, nums):
        sortedNums=sorted(nums)
        results=[]
        resultsDict={}

        while len(sortedNums)>2:
            target=-sortedNums[0]
            frontPointer=1
            backPointer=(len(sortedNums)-1)
            print('*************************************')
            print('Current sortesNums: '+str(sortedNums))
            print('Current target: '+str(target))
            print('Back and front pointers reset')
            

            while frontPointer<backPointer:
                twoSum=sortedNums[frontPointer]+sortedNums[backPointer]
                print('-------------------------------------------')
                print('TwoSum: '+str(twoSum))
                print('Analized range: '+str(sortedNums[frontPointer:backPointer+1]))

                if twoSum==target:
                    singleResult=tuple(sorted([-target,sortedNums[frontPointer],sortedNums[backPointer]]))
                    print('Detected results: '+str(singleResult))
                    results.append(list(singleResult))
                    #resultsDict[singleResult]=resultsDict.get(singleResult,0)+1
                    #if resultsDict[singleResult]==1:
                    #    results.append(list(singleResult))
                    #    print('Results without duplicates: '+str(results))
                    while frontPointer+1!=len(sortedNums)-1 and sortedNums[frontPointer]==sortedNums[frontPointer+1]:
                        frontPointer+=1
                        print('moved frontpointer in while: '+str(frontPointer))
                    frontPointer+=1
                    print('moved frontpointer outside while: '+str(frontPointer))
                    while backPointer-1!=0 and sortedNums[backPointer-1]==sortedNums[backPointer]:
                        backPointer-=1
                        print('moved backpointer in while: '+str(backPointer))
                    backPointer-=1
                    print('moved backpointer in while: '+str(backPointer))
                elif twoSum<target:
                    while frontPointer+1!=len(sortedNums)-1 and sortedNums[frontPointer]==sortedNums[frontPointer+1]:
                        frontPointer+=1
                    frontPointer+=1
                    print('moved frontpointer in twoSum<target: '+str(frontPointer))
                else:
                    while backPointer-1!=0 and sortedNums[backPointer-1]==sortedNums[backPointer]:
                        backPointer-=1
                    backPointer-=1
                    print('moved backpointer in twoSum>target: '+str(backPointer))
                print('Analized range: '+str(sortedNums[frontPointer:backPointer+1]))
                testing=[0,1]

            while len(sortedNums)>1 and sortedNums[0]==sortedNums[1]:
                del sortedNums[1]
            del sortedNums[0]

        return results
'''