class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        def pow(x, n):
            if n == 1:
                return x

            res = pow(x, n // 2)
            res = res * res
            if n % 2 == 1:
                res = res * x
            return res

        if n < 0:
            return 1 / pow(x, abs(n))
        else:
            return pow(x, n)