class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.word = "" # Falsy, can be treated as is_word

    def add_word(self, word):
        cur = self
        for char in word:
            index = ord(char) - ord('a')
            if not cur.chars[index]:
                cur.chars[index] = TrieNode()
            cur = cur.chars[index]
        cur.word = word # So that we don't have to build/un-build the string during dfs

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Create the Trie for the list of words.
        Go to each cell and perform DFS to find words.
        Use a visited array and do backtracking.
        """
        root = TrieNode()

        for word in words:
            root.add_word(word)

        res = set()
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(r, c, cur_trie_node):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            if (r, c) in visited:
                return

            # Pruning
            index = ord(board[r][c]) - ord('a')
            next_trie_node = cur_trie_node.chars[index]
            if not next_trie_node:
                return

            visited.add((r, c))

            if next_trie_node.word:
                res.add(next_trie_node.word)

            for d1, d2 in DIRECTIONS:
                dfs(r + d1, c + d2, next_trie_node)

            visited.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, root)

        return list(res)
