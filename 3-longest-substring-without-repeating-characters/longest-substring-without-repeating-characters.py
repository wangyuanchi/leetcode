class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexDict = {}
        longest = 0
        left = 0

        for i in range(len(s)):
            # check if the duplicate is still in the current window
            if s[i] in indexDict and indexDict[s[i]] >= left:
                left = indexDict[s[i]] + 1
            else:
                longest = max(longest, i - left + 1)
                
            indexDict[s[i]] = i

        return longest