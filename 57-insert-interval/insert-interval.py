class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Step 1: Insert
        added = False

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                added = True
                break
        
        if not added:
            intervals.append(newInterval)

        # Step 2: Merge
        start, end = 1, 0
        while start < len(intervals) and end < len(intervals) - 1:
            if intervals[start][0] > intervals[end][1]:
                start += 1
                end += 1
                continue
            
            # Overlap
            deleted = intervals.pop(start)
            intervals[end][1] = max(deleted[1], intervals[end][1])

        return intervals