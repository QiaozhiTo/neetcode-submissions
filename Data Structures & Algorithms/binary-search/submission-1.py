class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        nums.sort()
        while l < r:
            m = l + ((r-l) // 2)
            if nums[m] > target:
                r -= 1
            elif nums[m] < target:
                l += 1
            else:
                return m
        return -1
