class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = None
        while n != 0:
            bit = n % 2
            if prev_bit is None:
                prev_bit = bit
            else:
                if bit == prev_bit:
                    return False
                else:
                    prev_bit = bit
            n = n >> 1
        return True
