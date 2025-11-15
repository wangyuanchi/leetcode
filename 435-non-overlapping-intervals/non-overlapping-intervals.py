class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        r_val = intervals[0][1]
        remove_count = -1 # As the loop below always removes the first interval

        for interval in intervals:
            cur_l_val, cur_r_val = interval[0], interval[1]

            if cur_l_val < r_val:
                remove_count += 1
                # Simulate removing the larger overlapping interval
                # as removing larger interval will cause less conflicts later
                r_val = min(r_val, cur_r_val)
            else:
                r_val = cur_r_val

        return remove_count