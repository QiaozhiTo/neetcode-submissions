class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
                l = r
            maxP = max(maxP, prices[r] - prices[l])
        return maxP