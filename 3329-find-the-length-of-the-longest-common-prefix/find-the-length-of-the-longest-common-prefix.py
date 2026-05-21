class TrieNode:
    def __init__(self):
        self.children = [None] * 10
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, value: str):
        cur_node = self.root
        for c in value:
            index = ord(c) - ord("0")
            if cur_node.children[index]:
                cur_node = cur_node.children[index]
                continue
            
            cur_node.children[index] = TrieNode()
            cur_node = cur_node.children[index]
        cur_node.is_end = True

    def get_prefix(self, value: str):
        cur_node = self.root
        prefix_length = 0
        for c in value:
            index = ord(c) - ord("0")
            if cur_node.children[index]:
                cur_node = cur_node.children[index]
                prefix_length += 1
                continue
            return prefix_length
        return prefix_length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        lcp = 0
        for elem in arr1:
            trie.add(str(elem))
        for elem in arr2:
            lcp = max(lcp, trie.get_prefix(str(elem)))
        return lcp
        