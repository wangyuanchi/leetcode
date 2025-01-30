class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            middle = left + (right - left) // 2 # represents k
            if self.feasibleK(piles, h, middle): # try to lower
                right = middle
            else: # not feasible, have to increase
                left = middle + 1
        return left

    def feasibleK(self, piles: List[int], h: int, k: int) -> bool:
        requiredH = 0
        for bananas in piles:
            # don't use while loop and subtract 1 by 1 as it takes too long
            requiredH += math.ceil(bananas / k)
        return requiredH <= h