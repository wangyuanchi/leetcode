class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)

        valid_intervals = []
        heapq.heapify(valid_intervals)
        output_dict = {}

        cur_interval = 0
        for query in sorted(queries):
            # interval with start that > query is not valid
            while cur_interval < len(intervals) and intervals[cur_interval][0] <= query:
                start, end = intervals[cur_interval][0], intervals[cur_interval][1]
                length = end - start + 1
                heapq.heappush(valid_intervals, (length, end))
                cur_interval += 1

            # interval with end that < query is not valid
            # since queries is sorted, it won't be valid ever
            while len(valid_intervals) > 0:
                if valid_intervals[0][1] >= query:
                    break
                heapq.heappop(valid_intervals)

            # now, either heap is empty or has valid interval
            output_dict[query] = -1 if len(valid_intervals) == 0 else valid_intervals[0][0]

        return [output_dict[query] for query in queries]
            