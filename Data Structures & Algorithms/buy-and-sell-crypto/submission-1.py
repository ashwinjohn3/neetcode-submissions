class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            buy_price = prices[l]
            sell_price = prices[r]
            if buy_price < sell_price:
                profit = max(profit, sell_price - buy_price)
            else:
                l = r
            r += 1
        return profit
        