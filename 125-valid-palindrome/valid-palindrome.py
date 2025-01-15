class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = [c for c in s.lower() if c.isalnum()]
        
        left, right = 0, len(characters) - 1 
        while left < right:
            if characters[left] != characters[right]:
                return False
            else:
                left += 1
                right -= 1
        return True 