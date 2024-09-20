# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 756 ms, 27.46 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, buy, sell = 0, 0, 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                res = max(res, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return res
