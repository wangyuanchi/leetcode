class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        freq.sort(reverse=True)
        min_cost = 0
        for i in range(26):
            if freq[i] == 0:
                return min_cost
            min_cost += freq[i] * (i // 8 + 1)
        return min_cost
        
