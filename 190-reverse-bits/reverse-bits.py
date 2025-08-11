class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
             LSB = n & 1
             n = n >> 1
             res = res | LSB
             res = res << 1
        return res >> 1