# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         maxHeap = [-num for num in nums]
#         heapq.heapify(maxHeap)
#         while k > 1:
            
#             heapq.heappop(maxHeap)
#             k -= 1
#         return -maxHeap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]