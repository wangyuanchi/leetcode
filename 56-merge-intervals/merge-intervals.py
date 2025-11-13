class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []

        l_val, r_val = intervals[0][0], intervals[0][1]

        for interval in intervals:
            if interval[0] <= r_val:
                r_val = max(r_val, interval[1])
            else:
                res.append([l_val, r_val])
                l_val, r_val = interval[0], interval[1]

        # Add in the last interval
        res.append([l_val, r_val])

        return res