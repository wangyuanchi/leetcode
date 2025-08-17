class Solution:
    def climbStairs(self, n: int) -> int:
        # M**n, M[0][0] is f(n+1)
        # From examples, can see we want to return n+1th fibonacci number
        def matrix_multiplication(A, B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                    A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                    A[1][0] * B[0][1] + A[1][1] * B[1][1]]]
        
        def matrix_power(A, n):
            if n == 1:
                return A

            res = matrix_power(A, n // 2)
            res = matrix_multiplication(res, res)
            if n % 2 == 1:
                res = matrix_multiplication(res, A)
            return res
            

        M = [[1, 1], [1, 0]]
        res = matrix_power(M, n)
        return res[0][0]