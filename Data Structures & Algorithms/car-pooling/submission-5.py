class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minHeap = [] #[end, numPass]
        currPass = 0
        for passNum, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                currPass -= heapq.heappop(minHeap)[1]
            
            currPass += passNum
            if currPass > capacity:
                return False
            
            heapq.heappush(minHeap, [end, passNum])

        return True