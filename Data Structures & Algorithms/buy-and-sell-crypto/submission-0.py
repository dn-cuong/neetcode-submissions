class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for sell in range(1,len(prices)):
            if prices[sell] < buy:
                buy = prices[sell]
            ans = max(ans, prices[sell] - buy)
        return ans