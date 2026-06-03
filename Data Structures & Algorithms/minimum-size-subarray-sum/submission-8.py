# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         res = float('inf')
#         l, total = 0, 0
#         for r in range(len(nums)):
#             # total += nums[r]
#             while total > target:
#                 total -= nums[l] 
#                 l += 1
#             total += nums[r]
#             res = min(res, r - l + 1)

#         return res

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, total = 0, 0
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            
            # 第一次循环 total=0，while 直接跳过，nums[r] 才加进来，逻辑错位了。
            # total += nums[r]
            
        return 0 if res == float('inf') else res