class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        currentCarryOver = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += currentCarryOver
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
        
        # If I reach here, currentCarryOver must be 1
        digits.insert(0, 1)
        return digits