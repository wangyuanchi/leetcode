class MedianFinder:

    def __init__(self):
        self.total = 0
        self.median = None
        self.lower_half = [] # Max heap (negated values) (lower-heavy)
        self.upper_half = [] # Min heap
        heapq.heapify(self.lower_half)
        heapq.heapify(self.upper_half)

    def addNum(self, num: int) -> None:
        if self.total == 0:
            self.median = num
            heapq.heappush(self.lower_half, -num)
            self.total += 1
            return

        if self.total == 1:
            if num >= self.median:
                heapq.heappush(self.upper_half, num)
            else:
                transfer_value = -heapq.heappop(self.lower_half)
                heapq.heappush(self.upper_half, transfer_value)
                heapq.heappush(self.lower_half, -num)
                
            self.median = (self.median + num) / 2
            self.total += 1
            return

        # Now, total must be at least 2
        lower_max = -self.lower_half[0]
        upper_min = self.upper_half[0]

        # Need to maintain the invariant!
        if len(self.lower_half) == len(self.upper_half):
            if num <= lower_max:
                self.median = lower_max
                heapq.heappush(self.lower_half, -num)
            elif num <= upper_min:
                self.median = num
                heapq.heappush(self.lower_half, -num)
            else:
                self.median = upper_min
                transfer_value = heapq.heappop(self.upper_half)
                heapq.heappush(self.lower_half, -transfer_value)
                heapq.heappush(self.upper_half, num)
        else: # It must be the case that len(lower_half) > len(upper_half)
            if num <= lower_max:
                transfer_value = -heapq.heappop(self.lower_half)
                heapq.heappush(self.upper_half, transfer_value)
                heapq.heappush(self.lower_half, -num)
                self.median = (-self.lower_half[0] + transfer_value) / 2
            elif num <= upper_min:
                self.median = (num + lower_max) / 2
                heapq.heappush(self.upper_half, num)
            else:
                self.median = (lower_max + upper_min) / 2
                heapq.heappush(self.upper_half, num)
        
        self.total += 1

    def findMedian(self) -> float:
        return self.median
        