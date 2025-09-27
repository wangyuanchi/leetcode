class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Note: Python doesn't have an 32 bit limit,
        # so negative numbers are sign extended "forever" in 2s complement
        # Using the example of 1 + (-1), we can see that it will loop forever
        # So, we need to mask it.

        mask = 0xFFFFFFFF # 32 bits of "1"

        # Changing a and b in place
        while (a & b) & mask != 0:
            a, b = a ^ b, a & b
            b = b << 1
        ans = (a ^ b) & mask

        # Note that this mask prevented the leading "1"s.
        # Python will think this is a positive number, so we have to check.
        max_int = 0x7FFFFFFF
        if ans <= max_int:
            return ans
        else:
            return ~(ans ^ mask) # Sign extend with "1"
