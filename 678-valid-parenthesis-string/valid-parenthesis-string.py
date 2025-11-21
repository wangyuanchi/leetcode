class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        For normal check valid parenthesis, we keep a left counter.
        If while looping through string, if left < 0, then invalid.
        But now, because of the *, there's a range of values left can be.
        So, we can keep track of the range using min and max of left.
        If choosing * to be ) decreases min to < 0, then,
        it is invalid so we don't make this choice and keep min at 0.
        If ) appears and we have min at 0, then that decision branch
        is invalid. So, we keep min at 0 due to the branch from min 1.
        If at any point max < 0, it's invalid. Final check 0 in range.
        """
        min_left, max_left = 0, 0 # The range of possible count for (

        for char in s:
            if char == "(":
                min_left += 1
                max_left += 1
            elif char == "*":
                min_left = max(0, min_left - 1)
                max_left += 1
            else:
                min_left = max(0, min_left - 1)
                max_left -= 1
            
            if max_left < 0: # min_left is always >= 0
                return False
        
        return min_left == 0
