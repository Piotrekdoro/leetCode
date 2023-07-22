'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height):
        frontPointer=0
        backPointer=len(height)-1
        maxVolume=0
        curVolume=0

        while frontPointer<backPointer:
            curVolume=min([height[frontPointer],height[backPointer]])*(backPointer-frontPointer)
            if curVolume>=maxVolume:
                maxVolume=curVolume
            if height[frontPointer]<height[backPointer]:
                frontPointer+=1
            else:
                backPointer-=1
        return maxVolume


        



test=Solution().maxArea([1,8,6,2,5,4,8,3,7])#[1,1]
print(test)
