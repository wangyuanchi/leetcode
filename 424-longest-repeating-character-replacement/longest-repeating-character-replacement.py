class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {} # represents the current state of the substring
        maxLength = 0

        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            if right - left + 1 - max(freq.values()) <= k:
                maxLength = max(maxLength, right - left + 1)
            else:
                # shift the left pointer until condition <= k is satisfied
                while right - left + 1 - max(freq.values()) > k:
                    freq[s[left]] -= 1
                    left += 1
        
        return maxLength