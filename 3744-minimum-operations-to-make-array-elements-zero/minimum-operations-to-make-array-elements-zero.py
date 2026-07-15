class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def get_total_operations_until_n(n: int) -> int:
            # Example of a base: 0b1111, 0b111111
            prev_base, base = 0, 1 # prev_base is not considered in the current calculation
            bits_in_base = 1
            total_operations = 0
            
            while n > prev_base:
                operations_to_zero_for_base = math.ceil(bits_in_base / 2)
                total_in_range = min(n, base) - prev_base
                total_operations += operations_to_zero_for_base * total_in_range

                prev_base = base
                base = (base << 1) + 1
                bits_in_base += 1

            return total_operations

        res = 0
        for query in queries:
            res += math.ceil(
                (get_total_operations_until_n(query[1]) - get_total_operations_until_n(query[0] - 1)) / 2
            )
        
        return res