class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)

        count = 0

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break

        i = 0
        for j in range(1, len(s)):
            l = i
            r = j

            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break

            i += 1

        return count
