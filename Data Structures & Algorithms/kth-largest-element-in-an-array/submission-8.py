# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         minHeap = nums
#         heapq.heapify(minHeap)
#         while len(minHeap) > k:
#             heapq.heappop(minHeap)
#         return minHeap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        return -maxHeap[0]