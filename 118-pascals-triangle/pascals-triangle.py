class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
                continue
            if i == 1:
                res.append([1, 1])
                continue
            cur = [1]

            target_arr = res[i - 1]
            l, r = 0, 1

            while r < len(target_arr):
                cur.append(target_arr[l] + target_arr[r])
                l += 1
                r += 1

            cur.append(1)
            res.append(cur)

        return res