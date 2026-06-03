# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)-1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j] and abs(i-j) <= k:
#                     return True
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if (R - L) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
