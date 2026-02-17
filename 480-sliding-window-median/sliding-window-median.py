class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = [] # lower-half, heavy, negated values
        min_heap = [] # upper-half
        lazy_delete = {} # key: number, value: freq
        medians = []

        def append_median():
            if k % 2 == 0:
                medians.append((min_heap[0] - max_heap[0]) / 2)
            else:
                medians.append(-max_heap[0])

        # Fill up the first k numbers into the heaps
        for i in range(k):
            num = nums[i]
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

            if len(min_heap) == len(max_heap) + 1:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        append_median()

        for i in range(k, len(nums)):
            add_num, del_num = nums[i], nums[i - k]
            to_remove_min_heap, to_remove_max_heap = 0, 0

            # Add the current number
            if add_num > -max_heap[0]:
                heapq.heappush(min_heap, add_num)
                to_remove_min_heap = 1
            else:
                heapq.heappush(max_heap, -add_num)
                to_remove_max_heap = 1

            # Lazily delete the previous number
            if del_num not in lazy_delete:
                lazy_delete[del_num] = 0
            lazy_delete[del_num] += 1
            if del_num > -max_heap[0]:
                to_remove_min_heap -= 1
            else:
                to_remove_max_heap -= 1

            # Range of values for to_remove is between -1, 0 and 1
            # This operations balances our min and max heaps based only on valid values
            if to_remove_max_heap != 0: # Not Balanced
                if to_remove_max_heap == 1: # and to_remove_min_heap == -1
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
                else: # to_remove_max_heap == -1 and to_remove_min_heap == 1
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # Remove lazily deleted values if possible
            # This does not affect the balance as it is based on valid values
            while max_heap and -max_heap[0] in lazy_delete and lazy_delete[-max_heap[0]] > 0:
                lazy_delete[-heapq.heappop(max_heap)] -= 1

            while min_heap and min_heap[0] in lazy_delete and lazy_delete[min_heap[0]] > 0:
                lazy_delete[heapq.heappop(min_heap)] -= 1

            append_median()

        return medians
