class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonically decreasing queue
        q = deque()
        res = []

        for i in range(len(nums)):
            # Queue logic
            while len(q) > 0 and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
        
            # Calculating max logic
            if i + 1 >= k:
                start = i - k + 1 # First index in current window
                while q[0][1] < start:
                    q.popleft()
                res.append(q[0][0])

        return res