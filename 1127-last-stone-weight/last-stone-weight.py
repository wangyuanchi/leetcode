class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            if s1 == s2:
                continue

            if s1 > s2:
                heapq.heappush_max(stones, s1 - s2)
        
        return 0 if not stones else stones[0]
