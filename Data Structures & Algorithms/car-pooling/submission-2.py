class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        minHeap = []
        curPass = 0

        for passNum, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                curPass -=  heapq.heappop(minHeap)[1]
            curPass += passNum
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, passNum])

        return True