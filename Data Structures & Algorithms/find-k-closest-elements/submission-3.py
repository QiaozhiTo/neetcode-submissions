# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         l, r = 0, len(arr) - k
#         while l < r :
#             m = (l + r) // 2
#             if x - arr[m] > arr[m + k] - x:
#                 l = m + 1
#             else:
#                 r = m
#         return arr[l: l + k]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k :
            
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                 r-= 1
        return arr[l: r + 1]