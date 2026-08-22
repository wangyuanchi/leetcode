class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q = deque()
        q.append((0, 0, 0))
        upper_bound = max(x, max(forbidden or [])) + a + b
        visited = set()
        
        while len(q) > 0:
            position, was_prev_back, jumps = q.popleft()

            if position == x:
                return jumps

            forward_position = position + a
            backward_position = position - b
            if (
                forward_position not in forbidden and
                forward_position <= upper_bound and
                (forward_position, False) not in visited
            ):
                q.append((forward_position, False, jumps + 1))
                visited.add((forward_position, False))
            if (
                not was_prev_back and
                backward_position not in forbidden and 
                backward_position >= 0 and
                (backward_position, True) not in visited
            ):
                q.append((backward_position, True, jumps + 1))
                visited.add((backward_position, True))

        return -1