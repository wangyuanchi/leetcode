class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Early return
        if len(s1) + len(s2) != len(s3):
            return False

        # Since the lengths must add up now,
        # the index at s1 and s2 sums to the index at s3
        memo = {} # Key is (i1, i2)

        # Check if the s3[i1+i2:] can be formed from s1[i1:] and s2[i2:]
        def dp(i1, i2):
            i3 = i1 + i2

            # Base case
            if i1 == len(s1):
                return s2[i2:] == s3[i3:]

            if i2 == len(s2):
                return s1[i1:] == s3[i3:]

            # Memo
            if (i1, i2) in memo:
                return memo[(i1, i2)]

            # Main logic
            if s1[i1] != s3[i3] and s2[i2] != s3[i3]:
                memo[(i1, i2)] = False
            else:
                flag1, flag2 = False, False
                if s1[i1] == s3[i3]:
                    flag1 = dp(i1+1, i2)
                if s2[i2] == s3[i3]:
                    flag2 = dp(i1, i2+1)
                memo[(i1, i2)] = flag1 or flag2

            return memo[(i1, i2)]
                
        return dp(0, 0)