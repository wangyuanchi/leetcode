class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {} # key: i, val

        def dp(i, val):
            if (i, val) in memo:
                return memo[(i, val)]

            if i == 0:
                return 1

            max_case_1 = dp(i - 1, nums1[i - 1]) + 1 if val >= nums1[i - 1] else 1
            max_case_2 = dp(i - 1, nums2[i - 1]) + 1 if val >= nums2[i - 1] else 1

            memo[(i, val)] = max(max_case_1, max_case_2)
            return memo[(i, val)]

        res = 0
        for i in range(len(nums1)):
            res = max(res, dp(i, nums1[i]), dp(i, nums2[i]))
        
        return res