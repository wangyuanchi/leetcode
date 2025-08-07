class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict, window = {}, {}
        neededKeys, satisfiedKeys = 0, 0
        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                window[char] = 0
                tDict[char] = 1
                neededKeys += 1

        # First, find a valid substring
        # Then, to find a possible shorter substring,
        # shorten the substring from the left until it violates
        l, r = 0, 0 # s[l:r]
        shortest_l, shortest_r, shortest_length = 0, 0, 2**31 - 1
        # The "or" part is to satisfy the last left pointer slide
        while r < len(s) or neededKeys == satisfiedKeys:
            if neededKeys != satisfiedKeys:
                if s[r] in window:
                    window[s[r]] += 1
                    if window[s[r]] == tDict[s[r]]:
                        satisfiedKeys += 1
                r += 1
            else: # Current s[l:r] is a valid substring
                if r - l < shortest_length:
                    shortest_length = r - l
                    shortest_l, shortest_r = l, r
                
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] == tDict[s[l]] - 1:
                        satisfiedKeys -= 1
                l += 1

        return s[shortest_l:shortest_r]
