class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquareDigits(n):
            res = 0
            for digit in str(n):
                res += int(digit) ** 2
            return res
            
        checked = set()

        while n != 1:
            if n in checked:
                return False

            checked.add(n)
            n = sumSquareDigits(n)
            
        return True