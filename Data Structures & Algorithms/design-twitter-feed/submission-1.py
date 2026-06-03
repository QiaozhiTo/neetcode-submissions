class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                cnt, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([cnt,tweetId, followeeId, index-1])
        heapq.heapify(minHeap)          
        while minHeap and len(res) < 10:
            cnt, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            cnt, tweetId = self.tweetMap[followeeId][index]
            if index >= 0:
                heapq.heappush(minHeap, [cnt,tweetId, followeeId, index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
