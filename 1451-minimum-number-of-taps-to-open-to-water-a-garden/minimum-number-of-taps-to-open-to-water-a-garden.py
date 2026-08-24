class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)
        for i, rge in enumerate(ranges):
            left_boundary = max(0, i - rge)
            right_boundary = min(n, i + rge)
            max_reach[left_boundary] = max(max_reach[left_boundary], right_boundary)
        
        l, r = 0, 0 # The current inclusive range for the tap
        taps_opened = 0

        while r < n:
            taps_opened += 1
            prev_r = r
            for i in range(l, r + 1):
                r = max(r, max_reach[i])
            l = prev_r + 1

            if r < n and prev_r == r: # no progress
                return -1

        return taps_opened