class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python has no max heap implementation
        negative_stones = []
        for stone in stones:
            negative_stones.append(-stone)
        
        # min heap with negative numbers
        heapq.heapify(negative_stones)

        while len(negative_stones) > 1:
            stone1 = abs(heapq.heappop(negative_stones))
            stone2 = abs(heapq.heappop(negative_stones))
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(negative_stones, -(stone1 - stone2))
            else:
                heapq.heappush(negative_stones, -(stone2 - stone1))

        if len(negative_stones) == 1:
            return -negative_stones[0]
        else:
            return 0