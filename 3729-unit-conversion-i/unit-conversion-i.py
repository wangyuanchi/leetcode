class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for source, target, factor in conversions:
            adj_list[source].append((target, factor))
            adj_list[target].append((source, 1 / factor))

        q = deque()
        visited = set()
        q.append((0, 1))
        visited.add(0)
        resulting_conversions = [-1 for _ in range(len(conversions) + 1)]

        while len(q) > 0:
            unit, cumulative_factors = q.popleft()

            resulting_conversions[unit] = cumulative_factors

            for neighbour_unit, factor in adj_list[unit]:
                if neighbour_unit in visited:
                    continue

                visited.add(neighbour_unit)

                q.append((neighbour_unit, (cumulative_factors * factor) % (10**9 + 7)))

        return resulting_conversions