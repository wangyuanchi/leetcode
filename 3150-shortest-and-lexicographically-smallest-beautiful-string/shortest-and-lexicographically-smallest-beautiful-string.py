class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cur_k = 0
        length_res = float('inf')
        l_res = 0
        r_res = 0

        l = 0
        for r in range(len(s)):
            char = s[r]
            if char == "1":
                cur_k += 1
        
            while cur_k >= k:
                if cur_k == k and (
                    r - l + 1 < length_res or
                    (r - l + 1 == length_res and s[l:r+1] < s[l_res:r_res+1])
                ):
                    l_res = l
                    r_res = r
                    length_res = r - l + 1

                if s[l] == "1":
                    cur_k -= 1
                l += 1
        
        return "" if length_res == float('inf') else s[l_res:r_res+1]
                