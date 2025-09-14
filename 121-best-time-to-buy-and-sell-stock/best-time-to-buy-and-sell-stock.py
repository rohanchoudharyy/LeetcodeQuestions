class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = float('inf')
        max_profit = 0

        for i in prices:
            if i<lowest:
                lowest = i
            max_profit = max(max_profit,i-lowest)
        
        return max_profit