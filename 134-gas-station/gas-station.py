class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # Now, sum(gas) >= sum(cost)
        # There is at least 1 solution -> There is only 1 solution
        # Proof by prefix sum of diff
        
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        total, start = 0, 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total, start = 0, i + 1

        return start