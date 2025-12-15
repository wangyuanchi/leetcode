class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        For constructing the adjacency list, the naive method takes O(n^2*L),
        where n is the number of words and L is the length of a word.
        Assuming n >> L, this is very inefficient.
        Note: Forming a single word takes O(L)
        Instead, if we form a dictionary, where keys are of the form "*at"
        and values are of ["bat", "cat", "hat"], this takes O(n*L^2)
        BFS worst case takes O(V + E) = O(n + n*26L^2) = O(n*L^2)
        """
        # Form the adjacency list
        adj_list = {}
        for word in wordList: # O(n)
            word_arr = [c for c in word]
            for i, c in enumerate(word_arr): # O(L)
                word_arr[i] = "*"
                key = "".join(word_arr) # O(L)
                if key in adj_list:
                    adj_list[key].append(word)
                else:
                    adj_list[key] = [word]
                word_arr[i] = c

        # BFS (check visited before enqueueing)
        visited = set()
        visited.add(beginWord)
        transformations = 1
        q = [(beginWord, transformations)]

        while len(q) > 0:
            word, transformations = q.pop(0)

            # Base case
            if word == endWord:
                return transformations
            
            # Loop through the unvisited neighbours
            word_arr = [c for c in word]
            for i, c in enumerate(word_arr):
                word_arr[i] = "*"
                key = "".join(word_arr)
                neighbours = adj_list[key] if key in adj_list else []
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append((neighbour, transformations + 1))
                word_arr[i] = c

        return 0
