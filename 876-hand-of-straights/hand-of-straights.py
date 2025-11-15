class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        For this question, if the hands are all within a very small range
        We can use bucket sort to achieve O(n).
        However, in the general case, we cannot assume this.
        If some hand is small and another is very large, then it will be inefficient.
        The direct way is to find the smallest hand and start from there as
        it must be the start of a group.
        To keep track of this smallest hand requires sorting, which leads to O(nlogn).
        Instead of smallest hand, we can find the start of any group (less restrictive).
        To do this, start at the first hand and go backwards until you cannot anymore.
        This has to be the start of some group. But now, notice that
        we have in a sense found consecutive buckets, each having at least 1 value.
        We can do the bucket sort method (which might extend past our initial trigger)
        until there is no more next consecutive value, and the backtracking part is overshadowed.
        When we do this using an outer loop on hands, we are processing consecutive bulks
        by consecutive bulks. This results in O(n) overall.
        """
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for h in hand:
            if h not in freq:
                freq[h] = 1
            else:
                freq[h] += 1

        for h in hand:
            if freq[h] == 0:
                continue

            # Find the start that still have remaining cards
            start = h
            while start - 1 in freq and freq[start - 1] != 0:
                start -= 1
            
            # Loop through the consecutive "buckets"
            while start in freq:
                # Requires outer loop because there can be many groups that start from "start"
                while freq[start] != 0:
                    # Form groups from value "start" onwards
                    for val in range(start, start + groupSize):
                        if val not in freq or freq[val] == 0:
                            return False
                        else:
                            freq[val] -= 1
                start += 1

        return True