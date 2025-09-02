class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Calculating the total number of subarrays ending at the current index that match
        count = {}
        count[0] = 1

        # Create prefix sum
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
                continue
            prefix.append(nums[i] + prefix[i - 1])

        # Main logic
        total = 0
        for p in prefix:
            if p - k in count:
                total += count[p - k]
            
            if p not in count:
                count[p] = 1
            else:
                count[p] += 1

        return total