class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for pile in piles:
            max_heap.append(-pile)
        heapq.heapify(max_heap)

        for _ in range(k):
            pile = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ceil(pile / 2))

        return -sum(max_heap)
