#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_dict = dict() # (userId,[follow_list])
        self.post_list = [] # ((userId, tweetId))

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.post_list.append((userId, tweetId))
        if userId not in self.user_dict.keys():
            self.user_dict[userId] = [userId]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.user_dict.keys(): 
            return
        count = 0
        ret_list = []
        for user_id, tweet_id in self.post_list[-1 : -(len(self.post_list) + 1): -1]:
            if user_id in self.user_dict.get(userId):
                ret_list.append(tweet_id)
                print(ret_list)
                count += 1
                if count == 10:
                    break
        return ret_list
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_dict.keys():
            self.user_dict[followerId] = [followerId]
            self.user_dict[followerId].append(followeeId)
        else:
            self.user_dict[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId == followerId:
            return
        if followerId not in self.user_dict.keys():
            return
        if followeeId in self.user_dict.get(followerId):
            self.user_dict[followerId].remove(followeeId)
        else:
            return
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

