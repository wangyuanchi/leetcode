class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
            
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        
        required = 0
        for c, f in freq.items():
            if f % 2 == 1:
                required += 1

        return required <= k
    