class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        greater_index = 0
        while l < r:
            m = l + (r - l) // 2
            if letters[m] <= target:
                l = m + 1
                greater_index = m + 1
            else:
                r = m
                greater_index = m
        return letters[greater_index] if letters[greater_index] > target else letters[0]