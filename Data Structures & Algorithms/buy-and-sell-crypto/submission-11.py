class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, l = 0, 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            l + 1
        return maxP