class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0
        profit = 0
        for index, number in enumerate(prices):
            if number < prices[left_pointer]:
                left_pointer=index
            elif number> prices[left_pointer] :
                profit=max(profit,number-prices[left_pointer])
        
        return profit
    
    
    
    
    
    
    
 
