class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # want to do the most frequent task first
        # but also take note of the n cycles

        # use a max heap to get the most frequent task
        # note that we do not actually need to keep track of the task character
        freq_dict = {}
        for task in tasks:
            if task not in freq_dict:
                freq_dict[task] = -1
            else:
                freq_dict[task] -= 1
        heap = list(freq_dict.values())
        heapq.heapify(heap) # max heap that tracks frequency

        # whenever a task is done and still have more
        # add it to a queue with the time it can be completed again
        # and when it can be completed again, add it back to heap before popping
        cycles = 0
        queue = []

        while len(heap) > 0 or len(queue) > 0:
            if len(queue) > 0 and queue[0][0] == cycles:
                refreshed = queue.pop(0)
                heapq.heappush(heap, refreshed[1])

            if len(heap) > 0:
                max_freq = heapq.heappop(heap)

                # if still have the same type of task not completed
                if max_freq < -1:
                    completable_time = cycles + n + 1
                    freq = max_freq + 1
                    queue.append((completable_time, freq))

            cycles += 1

        return cycles