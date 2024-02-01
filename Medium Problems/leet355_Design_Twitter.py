# Description
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

# Solution

# // Time Complexity : 
# // Space Complexity : 
# // Did this code successfully run on Leetcode : 
# // Any problem you faced while coding this : 


# // Your code here along with comments explaining your approach
# Approach is 
from queue import PriorityQueue
class Twitter:

    class tweet:
        def __init__(self,tweetId,createdAt):
            self.tweetId = tweetId
            self.createdAt = createdAt

    def __init__(self):
        self.followList = {}
        self.tweetList = {}
        self.count = +1

    def postTweet(self, userId, tweetId):
        self.follow(userId,userId)
        if userId in self.tweetList:
            self.tweetList[userId].append(self.tweet(tweetId,self.count))
            self.count += 1
        else:
            self.tweetList[userId] = [self.tweet(tweetId,self.count)]
            self.count += 1
        

    def getNewsFeed(self, userId):
        newsFeed = PriorityQueue(11)

        if userId in self.followList:
            for userName in self.followList[userId]:
                if userName in self.tweetList:
                    n = len(self.tweetList[userName])
                    if n<10:
                        end = -1
                    else:
                        end = n-11
                    for i in range(n-1,end,-1):
                        newsFeed.put((self.tweetList[userName][i].createdAt,self.tweetList[userName][i].tweetId))
                        if newsFeed.qsize() > 10:
                            newsFeed.get()
        result = [0 for _ in range(newsFeed.qsize())]
        for i in range(newsFeed.qsize()-1,-1,-1):
            result[i] = newsFeed.get()[1]
        
        return result
        

    def follow(self, followerId, followeeId):
        if followerId in self.followList:
            if followeeId not in self.followList[followerId]:
                self.followList[followerId].add(followeeId)
        else:
            self.followList[followerId] = set()
            self.followList[followerId].add(followerId)
            self.followList[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followerId in self.followList:
            if followeeId in self.followList[followerId]:
                self.followList[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)