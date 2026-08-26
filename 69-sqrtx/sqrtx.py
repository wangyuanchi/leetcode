class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        best_guess = 0

        while l <= r:
            m = l + (r - l) // 2

            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
                best_guess = m
            else:
                r = m - 1

        return best_guess