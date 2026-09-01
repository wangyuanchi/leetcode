class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        matrix = [[1, 1],
                [1, 0]]
        power = n - 1

        res = self.calculate_power(matrix, power)
        return res[0][0]
    
    def calculate_power(self, matrix, power):
        if power == 1:
            return matrix

        res = self.calculate_power(matrix, power // 2)
        res = self.matmul(res, res)
        if power % 2 == 1:
            res = self.matmul(res, matrix)
        return res

    def matmul(self, A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]