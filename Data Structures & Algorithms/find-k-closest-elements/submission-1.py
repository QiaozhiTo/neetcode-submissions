# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         l, r = 0, len(arr) - k
#         while l < r:
#             m = (l + r) // 2
#             if x - arr[m] > arr[m+k] - x:
#                 l = m + 1
#             else:
#                 r = m
#         return arr[l: l+k]
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while r - l + 1 > k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l: r+1]