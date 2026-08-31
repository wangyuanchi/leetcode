class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 0
        odd = 0
        res = 0

        # when updating, always consider even odd and res
        for i, val in enumerate(arr):
            if val % 2 == 0:
                even += 1
                res += odd
            else:
                prev_odd = odd
                odd = even + 1
                even = prev_odd
                res += odd

        return res % (10**9 + 7)