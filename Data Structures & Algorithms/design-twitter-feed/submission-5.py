class Twitter:

    def __init__(self):
        self.post_dict = {}
        self.follower_dict = {}
        self.num = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post_dict:
            self.post_dict[userId] = [(self.num, tweetId)]
        else:
            self.post_dict[userId].append((self.num, tweetId))
        self.num -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follower_dict:
            self.follower_dict[userId] = set([userId])
        else:
            self.follower_dict[userId].add(userId)
        heap = []
        for followee in self.follower_dict[userId]:
            if followee not in self.post_dict:
                continue
            num_tweets = len(self.post_dict[followee])
            if num_tweets == 0:
                continue
            index = num_tweets - 1
            num, last_tweet = self.post_dict[followee][index]
            heapq.heappush(heap, (num, last_tweet, followee, index))
        
        res = []
        n = 0
        while n < 10 and heap:
            num, tweetId, followee, index = heapq.heappop(heap)
            res.append(tweetId)
            if index > 0:
                index -= 1
                followee_tweets = self.post_dict[followee]
                num, last_tweet = followee_tweets[index]
                heapq.heappush(heap, (num, last_tweet, followee, index))
            n += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_dict:
            self.follower_dict[followerId].add(followeeId)
        else:
            self.follower_dict[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_dict and followeeId in self.follower_dict[followerId]:
            self.follower_dict[followerId].remove(followeeId)
        
