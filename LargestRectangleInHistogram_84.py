'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
class Solution:
    def largestRectangleArea(self, heights):
        
        maxArea=0
        popCounter=0

        histogramStack=[]

        i=1
        while True:

            if heights[i]>=heights[i-1]:
                histogramStack.append(heights[i-1])
                #here I should trigger another recount when I hit the end
                i+=1
            else:
                while histogramStack!=[] and histogramStack[len(histogramStack)-1]>heights[i]:
                    histogramStack.pop()
                    popCounter+=1



test=Solution().largestRectangleArea([2,1,5,6,2,3])
print(test)








'''
# Works but is too slow

class Solution:
    def largestRectangleArea(self, heights):
        rectangles=[]
        maxHeight=max(heights)
        widthBeginning=-1
        widthEnding=-1

        if maxHeight==0:
            return 0

        for layerNum in range(maxHeight):
            print('*********************************')
            print('layerNum: '+str(layerNum))
            for histogramNum in range(len(heights)):
                print('............................')
                print('histogramNum: '+str(histogramNum))
                if heights[histogramNum]-1>=layerNum:
                    if widthBeginning==-1:
                        widthBeginning=histogramNum
                        print('widthBeginning: '+str(widthBeginning))
                if heights[histogramNum]-1<layerNum:
                    if widthBeginning!=-1:
                        widthEnding=histogramNum-1
                        print('widthEnding: '+str(widthEnding))
                        rectangles.append((widthEnding-widthBeginning+1)*(layerNum+1))
                        print('Rectangles: '+str(rectangles))
                        widthBeginning=-1
                if widthBeginning!=-1 and histogramNum==len(heights)-1:
                    widthEnding=histogramNum
                    print('widthEnding: '+str(widthEnding))
                    rectangles.append((widthEnding-widthBeginning+1)*(layerNum+1))
                    print('Rectangles: '+str(rectangles))
                    widthBeginning=-1

        print(rectangles)
        return max(rectangles)
    
test=Solution()
print(test.largestRectangleArea([2,1,5,6,2,3]))
'''
