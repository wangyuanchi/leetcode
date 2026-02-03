class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        furthest = {}

        for index, char in enumerate(s):
            furthest[char] = index

        l, r = 0, 0
        start = 0
        res = []

        while start != len(s):
            r = max(r, furthest[s[l]])

            if l != r:
                l += 1
                continue

            res.append(r - start + 1)
            l, r = l + 1, r + 1
            start = l
        
        return res