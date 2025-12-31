class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        mismatched = len(freq)
        l_res_index, r_res_index = 0, len(s)
        l = 0

        for r in range(len(s)):
            r_char = s[r]
            if r_char not in freq:
                continue
            freq[r_char] -= 1

            if freq[r_char] == 0:
                mismatched -= 1

            if mismatched > 0:
                continue

            while mismatched == 0:
                if r - l < r_res_index - l_res_index:
                    l_res_index, r_res_index = l, r

                l_char = s[l]
                l += 1

                if l_char in freq:
                    freq[l_char] += 1
                    if freq[l_char] == 1:
                        mismatched += 1

        return "" if r_res_index == len(s) else s[l_res_index:r_res_index + 1]
