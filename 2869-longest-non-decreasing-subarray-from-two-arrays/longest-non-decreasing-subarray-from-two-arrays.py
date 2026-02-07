class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        arr = [[1 for _ in range(len(nums1))] for _ in range(2)]
        max_res = 1

        for i in range(1, len(nums1)):
            res1 = 1 if nums1[i] < nums1[i - 1] else arr[0][i - 1] + 1
            res2 = 1 if nums1[i] < nums2[i - 1] else arr[1][i - 1] + 1
            arr[0][i] = max(res1, res2)

            res1 = 1 if nums2[i] < nums1[i - 1] else arr[0][i - 1] + 1
            res2 = 1 if nums2[i] < nums2[i - 1] else arr[1][i - 1] + 1
            arr[1][i] = max(res1, res2)

            max_res = max(max_res, arr[0][i], arr[1][i])

        return max_res