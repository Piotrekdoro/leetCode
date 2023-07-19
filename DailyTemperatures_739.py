'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
class Solution:
    def dailyTemperatures(self, temperatures):
        unknownTemps=[]
        res=[0]*len(temperatures)
        
        for i in range(len(temperatures)):
            if unknownTemps==[]:
                unknownTemps.append((temperatures[i],i))
                continue
            while unknownTemps!=[] and temperatures[i]>unknownTemps[len(unknownTemps)-1][0]:
                res[unknownTemps[len(unknownTemps)-1][1]]=i-unknownTemps[len(unknownTemps)-1][1]
                del(unknownTemps[len(unknownTemps)-1])
            unknownTemps.append((temperatures[i],i))
        return res
    
test=Solution()
print(test.dailyTemperatures([73,74,75,71,69,72,76,73])) #Expected: [1,1,4,2,1,1,0,0]