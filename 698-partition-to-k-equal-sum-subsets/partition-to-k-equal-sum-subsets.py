class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)

        if sum(nums) % k:
            return False

        subset_sum = sum(nums) // k

        arr = []
        sum_dict = {}

        for i in range(k):
            arr.append([])
            sum_dict[i] = 0

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if sum_dict[j] + nums[i] > subset_sum:
                    continue
                
                arr[j].append(nums[i])
                sum_dict[j] += nums[i]
                if backtrack(i + 1):
                    return True
                sum_dict[j] -= nums[i]
                arr[j].pop()

                if not arr[j]:
                    break

            return False

        return backtrack(0)        