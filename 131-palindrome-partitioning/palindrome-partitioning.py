class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        # [l, r)
        def dfs(l, r):
            # Base case
            if r == len(s) + 1:
                if l != len(s):
                    return
                for substring in partition:
                    if not self.isPalindrome(substring):
                        return
                res.append(partition.copy())
                return

            # Substring is in the partition
            partition.append(s[l:r])
            dfs(r, r + 1)

            # Substring is not in the partition
            partition.pop()
            dfs(l, r + 1)

        dfs(0, 1)
        return res
    
    def isPalindrome(self, substring):
        l, r = 0, len(substring) - 1
        while l < r:
            if substring[l] != substring[r]:
                return False
            l += 1
            r -= 1
        return True
