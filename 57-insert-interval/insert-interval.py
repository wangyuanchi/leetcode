class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
            
        new_start, new_end = newInterval
        for index, interval in enumerate(intervals):
            start, end = interval
            if start >= new_start:
                intervals.insert(index, newInterval)
                break
            if index == len(intervals) - 1:
                intervals.append(newInterval)

        output_intervals = []

        l, r = 0, 1
        while r < len(intervals):
            l_start, l_end = intervals[l]
            r_start, r_end = intervals[r]
            if l_end >= r_start:
                intervals[r] = [l_start, max(l_end, r_end)]
            else:
                output_intervals.append(intervals[l])
            l += 1
            r += 1
        
        output_intervals.append(intervals[l])

        return output_intervals