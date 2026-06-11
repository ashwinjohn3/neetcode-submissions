class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        for i in range(len(prices) - 1):
            temp = prices[i+1] - prices[i]
            if temp > 0:
                totalProfit += temp
        return totalProfit
        