class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        l = len(prices)
        def dfs(i, buying):
            if i >= l: 
                return 0 
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                profit = dfs(i+1, False) - prices[i]
                max_profit = max(profit, cooldown)
                dp[(i, buying)] = max_profit
            else:
                profit = dfs(i+2, True) + prices[i]
                max_profit = max(profit, cooldown)
                dp[(i, buying)] = max_profit

            return dp[(i, buying)]

        return dfs(0, True)