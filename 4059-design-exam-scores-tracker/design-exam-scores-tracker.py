class ExamTracker:

    def __init__(self):
        self.prefix_sum = [] # Values are a tuple of (current time, actual prefix sum)

    def record(self, time: int, score: int) -> None:
        if not self.prefix_sum:
            self.prefix_sum.append((time, score))
        else:
            self.prefix_sum.append((time, score + self.prefix_sum[-1][1]))

    def totalScore(self, startTime: int, endTime: int) -> int:
        start_index = self.bin_search_suc(startTime)
        end_index = self.bin_search_pred(endTime)


        if start_index == -1 or end_index == -1:
            return 0

        if start_index == 0:
            return self.prefix_sum[end_index][1]
        else:
            return self.prefix_sum[end_index][1] - self.prefix_sum[start_index - 1][1] 
    
    def bin_search_suc(self, target_time) -> int:
        if target_time > self.prefix_sum[-1][0]:
            return -1

        l = 0
        r = len(self.prefix_sum) - 1
        potential_suc = len(self.prefix_sum) - 1

        while l <= r:
            m = l + (r - l) // 2 # low middle

            if (self.prefix_sum[m][0] == target_time):
                return m
            elif (self.prefix_sum[m][0] < target_time):
                l = m + 1
            else:
                r = m - 1
                potential_suc = m

        return potential_suc

    def bin_search_pred(self, target_time) -> int:
        if target_time < self.prefix_sum[0][0]:
            return -1

        l = 0
        r = len(self.prefix_sum) - 1
        potential_pred = 0

        while l <= r:
            m = l + (r - l) // 2 # low middle

            if (self.prefix_sum[m][0] == target_time):
                return m
            elif (self.prefix_sum[m][0] < target_time):
                l = m + 1
                potential_pred = m
            else:
                r = m - 1 

        return potential_pred



# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)