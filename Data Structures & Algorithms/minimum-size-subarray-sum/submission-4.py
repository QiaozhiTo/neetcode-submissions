class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        resLen = float('inf')
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                resLen = min(resLen, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if resLen == float("inf") else resLen