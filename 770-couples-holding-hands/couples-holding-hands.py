class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        a, b = 0, 1
        seats = []
        person_to_seat = {}

        while b < len(row):
            seats.append((row[a], row[b]))
            person_to_seat[row[a]] = (row[a], row[b])
            person_to_seat[row[b]] = (row[a], row[b])
            a += 2 
            b += 2

        adj_list = defaultdict(list)
        for seat in seats:
            if seat[0] == seat[1]:
                continue

            first_person = seat[0]
            second_person = seat[1]
            first_person_neighbour = first_person + 1 if first_person % 2 == 0 else first_person - 1
            second_person_neighbour = second_person + 1 if second_person % 2 == 0 else second_person - 1
            first_person_neighbour_seat = person_to_seat[first_person_neighbour]
            second_person_neighbour_seat = person_to_seat[second_person_neighbour]
            if first_person_neighbour_seat == second_person_neighbour_seat:
                adj_list[seat].append(first_person_neighbour_seat)
            else:
                adj_list[seat].append(first_person_neighbour_seat)
                adj_list[seat].append(second_person_neighbour_seat)

        visited = set()

        def dfs(seat):
            if seat in visited:
                return

            visited.add(seat)

            for neighbour_seat in adj_list[seat]:
                dfs(neighbour_seat)

        num_connected_components = 0
        for seat in seats:
            if seat not in visited:
                dfs(seat)
                num_connected_components += 1

        return len(seats) - num_connected_components
