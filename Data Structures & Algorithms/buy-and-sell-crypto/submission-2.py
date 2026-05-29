class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for selling in prices:
            profit = selling - min_buy
            max_profit = max(max_profit, profit)
            min_buy = min(selling, min_buy)
        
        return max_profit
        