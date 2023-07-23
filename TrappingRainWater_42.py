'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

'''
class Solution:
    def trap(self, height):
        frontPointer=-1
        backPointer=-1
        localHeightFront=0
        #localHeightBack=0
        #localWaterFront=0
        localWater=0
        totalWater=0

        if len(height)<=2:
            return 0

        for i in range(len(height)-2):
            if height[i]>height[i+1]:
                frontPointer=i
                localHeightFront=height[frontPointer]
                break
        if frontPointer==-1:
            return 0

        for j in reversed(range(frontPointer+1,len(height))):
            if height[j]>height[j-1]:
                backPointer=j
                localHeightBack=height[backPointer]
                break
        if backPointer==-1:
            return 0

        print('initial frontpointer: '+str(frontPointer))
        print('initial backpointer: '+str(backPointer))
        print('initial localheightfront: '+str(localHeightFront))
        print('initial localheightback: '+str(localHeightBack))
        print('------------------------------------------------')

        frontPointer+=1
        backPointer-=1
        print('frontpointer moved to: '+str(frontPointer))
        print('backpointer moved to: '+str(backPointer))
        print('**************************************************')

        
        if backPointer==frontPointer:
            return min(height[frontPointer-1],height[backPointer+1])-height[frontPointer]

        while frontPointer<backPointer:#I have to rewrite this so that I check if index of localHeightFront is smaller then index of localHeightBack
                print('Outer loop started, frontPointer<backPointer')
                if localHeightFront>=localHeightBack:
                    print('Backpointer condition met localHeightFront>=localHeightBack')
                    while height[backPointer]<localHeightBack:
                        print('Entered backpointer loop ')
                        localWater+=localHeightBack-height[backPointer]
                        backPointer-=1
                        print('backpointer moved in loop to: '+str(backPointer))
                    localHeightBack=height[backPointer]
                    print('Localheightback set to: '+str(localHeightBack))
                    totalWater+=localWater
                    print('Added local water: '+str(localWater)+' to total water making it: '+str(totalWater))
                    localWater=0
                    backPointer-=1
                    print('backpointer moved out of loop to: '+str(backPointer))

                else:
                    print('Frontpointer condition met in else clause')
                    while height[frontPointer]<localHeightFront:
                        print('Entered frontpointer loop ')
                        localWater+=localHeightFront-height[frontPointer]
                        frontPointer+=1
                        print('frontpointer moved in loop to: '+str(frontPointer))
                    localHeightFront=height[frontPointer]
                    print('Localheightfront set to: '+str(localHeightFront))
                    totalWater+=localWater
                    print('Added local water: '+str(localWater)+' to total water making it: '+str(totalWater))
                    localWater=0
                    frontPointer+=1
                    print('frontpointer moved out of loop to: '+str(frontPointer))
                print('**************************************************')
        print('Exited outer loop')
        print('Final frontpointer: '+str(frontPointer))
        print('Final backpointer: '+str(backPointer))
        print('Final localheightfront: '+str(localHeightFront))
        print('Final localheightback: '+str(localHeightBack))
        print('Final total water: '+str(totalWater))
        print('**************************************************')
        if backPointer==frontPointer and height[frontPointer]<=min(height[frontPointer-1],height[backPointer+1]):
            totalWater+=min(height[frontPointer-1],height[backPointer+1])-height[frontPointer]
        return totalWater

#test=Solution().trap([9,6,6,8,8,5,6,3])
test=Solution().trap([0,2,5,0,6,9,8,7,4,4,5,6])#10
print(test)



'''
#Works bur is to slow
class Solution:
    def trap(self, height):
        startHole=0
        endHole=1
        curHoleWater=0
        TotalWater=0
        localMaxHeight=[0,0]
        #print('Total water: '+str(TotalWater))
        #print('Total water: '+str(TotalWater))

        #I need to save all the heights into heightPairs dict then sort the ones that appear more then once and if the dict is empty break, if not select biggest height and put it as starthole
        #idea: I could also add curHoleWater to another dict and add it only after hole is complete
        if len(height)<2:
            return 0

        while True:
            if height[endHole]>=height[startHole]:
                localMaxHeight=[0,0]
                TotalWater+=curHoleWater
                print('added: '+str(curHoleWater)+' to totalwater making it: '+str(TotalWater))
                curHoleWater=0
                if endHole+1==len(height):
                    break
                startHole=endHole
                print('moved starthole to: '+str(startHole))
                endHole=startHole+1
                print('moved endhole to: '+str(endHole))

            else:
                curHoleWater+=height[startHole]-height[endHole]
                if height[endHole]>localMaxHeight[0]:
                    localMaxHeight[0]=height[endHole]
                    localMaxHeight[1]=endHole
                if endHole+1==len(height):
                    if localMaxHeight==[0,0]:
                        break                  
                    curHoleWater=0
                    print('triggered')
                    for i in range(startHole+1,localMaxHeight[1]):
                        curHoleWater+=localMaxHeight[0]-height[i]
                    TotalWater+=curHoleWater
                    curHoleWater=0
                    print('added: '+str(curHoleWater)+' to totalwater making it: '+str(TotalWater))
                    startHole=localMaxHeight[1]
                    endHole=startHole
                    print('moved starthole to: '+str(startHole))
                    print('moved endhole to: '+str(endHole))
                    if startHole+1==len(height):
                        break
                    localMaxHeight=[0,0]
                endHole+=1
                print('moved endhole to: '+str(endHole))
        
        return TotalWater
'''