class Solution:
    def reverse(self, x: int) -> int:
        x_string = str(abs(x))
        x_string = x_string[::-1]
        res = int(x_string) if x >= 0 else -int(x_string)
        if res > 2**31 - 1 or res < -2**31:
            return 0
        else:
            return res