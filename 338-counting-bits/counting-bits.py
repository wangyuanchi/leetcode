class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        0 - 0000 - 0
        1 - 0001 - 1 + dp[i - 1]
        2 - 0010 - 1 + dp[i - 2]
        3 - 0011 - 1 + dp[i - 2]
        4 - 0100 - 1 + dp[i - 4]
        5 - 0101 - 1 + dp[i - 4]
        6 - 0110 - 1 + dp[i - 4]
        7 - 0111 - 1 + dp[i - 4]
        8 - 1000 - 1 + dp[i - 8]
        Repeated work can be seen for the 2 LSB from 4 to 7 in 0 to 3
        '''
        res = [0 for _ in range(n + 1)]
        c = 1
        for i in range(1, len(res)):
            if c * 2 == i:
                c = i
            res[i] = 1 + res[i - c]
        return res