class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1
        window_dist = 0
        min_window_dist = float("inf")
        res_l, res_r = 0, k - 1

        # precalculate window_dist for first window
        for i in range(k):
            window_dist += abs(arr[i] - x)

        while r < len(arr):
            if r > k - 1: 
                window_dist -= abs(arr[l - 1] - x)
                window_dist += abs(arr[r] - x)

            if window_dist < min_window_dist:
                res_l = l
                res_r = r
                min_window_dist = window_dist
            l += 1
            r += 1

        return arr[res_l:res_r + 1]