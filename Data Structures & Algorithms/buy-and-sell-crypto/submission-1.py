# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfit = 0
#         for i in range(len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 maxProfit = max(maxProfit, prices[j] -prices[i])
#         return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r

            r += 1
        return res