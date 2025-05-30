class ListNode:
    
    def __init__(self, time, tweetId, next=None):
        self.time = time
        self.tweetId = tweetId
        self.next = next

class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = ListNode(self.time, tweetId)
        else:
            head = self.tweets[userId]
            self.tweets[userId] = ListNode(self.time, tweetId, head)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] # min heap of size 10 
        heapq.heapify(heap)
        
        followed_users = [userId]
        if userId in self.followers:
            followed_users = list(self.followers[userId])
            # if not following himself then add to followed_users for processing
            if userId not in followed_users:
                followed_users.append(userId)

        for user in followed_users:
            if user not in self.tweets:
                continue

            user_tweet = self.tweets[user] # ListNode
            while user_tweet:
                if len(heap) < 10:
                    heapq.heappush(heap, (user_tweet.time, user_tweet.tweetId))
                else:
                    if user_tweet.time > heap[0][0]: # is the current tweet later
                        heapq.heappop(heap)
                        heapq.heappush(heap, (user_tweet.time, user_tweet.tweetId))
                    else: # all tweets from this node onwards will not make the most recent 10
                        break
                
                user_tweet = user_tweet.next
        
        # heap has size 10 but not sorted
        sorted_heap = sorted(heap, key=lambda x: x[0], reverse=True)
        most_recent = []
        for elem in sorted_heap:
            most_recent.append(elem[1])

        return most_recent

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # deal with cases where can unfollow without following anyone
        if followerId not in self.followers:
            return
            
        # deal with cases where can unfollow without first being followed
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)