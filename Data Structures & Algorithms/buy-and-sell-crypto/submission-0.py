class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestbuy = prices[0]
        best_profit = 0 

        for p in prices: 
            if p < lowestbuy:
                lowestbuy = p
            else: 
                best_profit = max(best_profit, p - lowestbuy)
        
        return best_profit

        