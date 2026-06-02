class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = 0

        for i in prices:
            low=min(low,i)
            profit = i-low
            high = max(high,profit)

        return high