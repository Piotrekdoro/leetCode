'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
#Optimized for runtime
class Solution:
    def maxProfit(self, prices):
        
        maxProf=0
        maxPrice=prices[0]
        minPrice=prices[0]
        maxProfit=0

        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                if maxPrice-minPrice>maxProf:
                    maxProf=maxPrice-minPrice
                maxPrice=prices[i]
                minPrice=prices[i]
            else:
                if prices[i]>maxPrice:
                    maxPrice=prices[i]
        if maxPrice-minPrice>maxProf:
            maxProf=maxPrice-minPrice

        return maxProf







#test=Solution().maxProfit([7,1,5,3,6,4])
test=Solution().maxProfit([7,6,4,3,1])

print(test)




'''
#Optimized for memory
class Solution:
    def maxProfit(self, prices):
        
        maxProf=0

        while len(prices)>=1:
            curMaxPrice=max(prices)
            startingPrice=prices[0]
            if maxProf<=curMaxPrice-startingPrice:
                maxProf=curMaxPrice-startingPrice
            
            while len(prices)>=2:
                print(prices)
                if prices[1]>=startingPrice:
                    del prices[1]
                else:
                    break
            del prices[0]

        return maxProf
'''