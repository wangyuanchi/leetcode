class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [0, 0, 0]
        for triplet in triplets:
            # If any slot is > that in target, impossible to form target
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                merged = [max(merged[0], triplet[0]), max(merged[1], triplet[1]), max(merged[2], triplet[2])]
            if merged[0] == target[0] and merged[1] == target[1] and merged[2] == target[2]:
                return True
        return False