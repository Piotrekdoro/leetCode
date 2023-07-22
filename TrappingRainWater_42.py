'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

'''
class Solution:
    def trap(self, height):
        startHole=0
        endHole=1
        curHoleWater=0
        TotalWater=0
        heightpairs={}
        #print('Total water: '+str(TotalWater))
        #print('Total water: '+str(TotalWater))

        #I need to save all the heights into heightPairs dict then sort the ones that appear more then once and if the dict is empty break, if not select biggest height and put it as starthole
        #idea: I could also add curHoleWater to another dict and add it only after hole is complete

        while True:
            if height[endHole]>=height[startHole]:
                TotalWater+=curHoleWater
                curHoleWater=0
                if endHole+1==len(height)-1:
                    break
                startHole=endHole
                endHole=startHole+1
            else:
                curHoleWater+=height[startHole]-height[endHole]
                if endHole+1==len(height)-1:
                    break
                endHole+=1

        return TotalWater

test=Solution().trap([0,1,0,2,1,0,1,3,2])
print(test)