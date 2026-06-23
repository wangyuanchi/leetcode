# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = len(words)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        def find_char_match_count(a: str, b: str) -> int:
            count = 0
            for i in range(6):
                if a[i] == b[i]:
                    count += 1
            return count

        # prepopulate matrix
        for row in range(n):
            for col in range(n):
                matrix[row][col] = find_char_match_count(words[row], words[col])

        possible_indexes = set()
        for i in range(n):
            possible_indexes.add(i)

        def find_max_freq_from_row(row_id: int, indexes_to_search: set[int]) -> int:
            freq = defaultdict(int)
            for i in range(n):
                if i in indexes_to_search:
                    freq[matrix[row_id][i]] += 1
            return max(freq.values())

        def find_row_with_lowest_max_freq() -> int:
            row_id, max_freq = 0, find_max_freq_from_row(0, possible_indexes)
            for i in range(1, n):
                cur_freq = find_max_freq_from_row(i, possible_indexes)
                if cur_freq < max_freq:
                    max_freq = cur_freq
                    row_id = i
            return row_id

        while len(possible_indexes) > 1:
            row_id_guess = find_row_with_lowest_max_freq()
            matched_count = master.guess(words[row_id_guess])
            if matched_count == 6:
                return

            next_possible_indexes = set()
            for i in possible_indexes:
                if matrix[row_id_guess][i] == matched_count:
                    next_possible_indexes.add(i)
            possible_indexes = next_possible_indexes
        
        master.guess(words[possible_indexes.pop()])
