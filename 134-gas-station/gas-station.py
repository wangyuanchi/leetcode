class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        station_count = len(gas)
        for i in range(station_count):
            diff.append(gas[i] - cost[i])
        diff *= 2

        start_index = 0
        end_index = start_index + station_count
        cur_gas = 0

        for i, d in enumerate(diff):
            if start_index >= station_count:
                return -1
            
            # Valid starting point if possible to reach end_index with non-negative cur gas
            if i == end_index and cur_gas >= 0:
                return start_index

            cur_gas += d
            if cur_gas < 0:
                cur_gas = 0
                start_index = i + 1
                end_index = start_index + station_count
