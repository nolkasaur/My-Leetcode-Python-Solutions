# https://leetcode.com/problems/design-twitter/
# 0 ms, 16.73 MB

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_hashmap = defaultdict(list)
        self.follow_hashset = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_hashmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, min_heap = [], []
        self.follow_hashset[userId].add(userId)
        for followee_id in self.follow_hashset[userId]:
            if followee_id in self.tweet_hashmap:
                index = len(self.tweet_hashmap[followee_id]) - 1 # latest tweet from that user
                count, tweet_id = self.tweet_hashmap[followee_id][index]
                min_heap.append([count, tweet_id, followee_id, index - 1])
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.tweet_hashmap[followee_id][index]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_hashset[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_hashset[followerId]:
            self.follow_hashset[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
