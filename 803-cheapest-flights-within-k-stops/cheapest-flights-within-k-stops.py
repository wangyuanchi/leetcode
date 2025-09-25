class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # For Bellman-Ford:
        # From class: After k iterations, the nodes that are within k jumps in the
        # shortest path tree have the correct distance estimates.
        # More generic statement: After k iterations, the distance estimate is equal to
        # the weight of the shortest path from source to target that uses at most k edges.

        # Set up estimates array
        est = [2**30 for _ in range(n)]
        est[src] = 0

        for _ in range(k + 1):
            est_copy = est.copy()
            for edge in flights:
                # Relaxation. Note! Throughout 1 iteration, the relaxation uses the from_estimate
                # from the previous iteration, but the to_estimate always updates and uses the latest.
                from_i, to_i, price_i = edge[0], edge[1], edge[2]
                if est[from_i] + price_i < est_copy[to_i]:
                    est_copy[to_i] = est[from_i] + price_i
            est = est_copy

        return est[dst] if est[dst] != 2**30 else -1