class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        freq = {}
        max_freq = 0
        
        # l and r maintains the best current window size
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            max_freq = max(max_freq, freq[s[r]])
            
            window_length = r - l + 1
            if window_length - max_freq <= k:
                longest = max(longest, window_length)
            else:
                freq[s[l]] -= 1
                l += 1

        return longest
