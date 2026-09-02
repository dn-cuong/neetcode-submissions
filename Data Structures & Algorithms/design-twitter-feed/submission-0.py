import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        # userId -> set of users they follow
        self.following = defaultdict(set)

        # userId -> list of (time, tweetId)
        self.tweets = defaultdict(list)

        # global timestamp
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        # Store newest tweet with increasing timestamp
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        # User sees their own tweets
        # + tweets from everyone they follow
        users = self.following[userId] | {userId}

        # Put the most recent tweet from each user into heap
        for user in users:
            if user in self.tweets and self.tweets[user]:
                time, tweetId = self.tweets[user][-1]

                # Negative time because heapq is a min-heap
                heapq.heappush(heap, (-time, tweetId, user, len(self.tweets[user]) - 1))

        res = []

        # Get at most 10 newest tweets
        while heap and len(res) < 10:
            neg_time, tweetId, user, index = heapq.heappop(heap)

            res.append(tweetId)

            # Move to the previous tweet from this same user
            if index > 0:
                prev_time, prev_tweetId = self.tweets[user][index - 1]

                heapq.heappush(
                    heap,
                    (-prev_time, prev_tweetId, user, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)