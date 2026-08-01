class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        res = []
        nums.sort()
        prev_a = None
        for a in range(0, len(nums) - 3):
            if prev_a == nums[a]:
                continue
            prev_b = None
            for b in range(a + 1, len(nums) - 2):
                if prev_b == nums[b]:
                    continue

                c = b + 1
                d = len(nums) - 1

                while c < d:
                    cur_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if target == cur_sum:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                    elif target < cur_sum:
                        d -= 1
                    else:
                        c += 1

                prev_b = nums[b]
            prev_a = nums[a]
        return res