class Twitter:

    def __init__(self):
        self.post_heap = []
        self.post_num = 0
        self.follow_dict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.post_heap, (self.post_num, userId, tweetId))
        self.post_num -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap_copy = self.post_heap.copy()
        posts = []
        num = 0
        while num < 10 and heap_copy:
            post_num, post_userId, tweetId = heapq.heappop(heap_copy)
            if post_userId == userId or (userId in self.follow_dict and post_userId in self.follow_dict[userId]):
                posts.append(tweetId)
                num += 1
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_dict:
            self.follow_dict[followerId] = set([followeeId])
        else:
            self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_dict[followerId]:
            return
        self.follow_dict[followerId].remove(followeeId)
        
