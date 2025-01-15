class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        # First pass: Adding count
        for n in nums:
            if n in freqDict:
                freqDict[n] += 1
            else:
                freqDict[n] = 1

        # Second pass: Adding to buckets
        buckets = [[] for i in range((len(nums) + 1))]
        for key, val in freqDict.items():
            buckets[val].append(key)

        # Third pass: Get the most frequent k elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result