class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not curNode.children[index]:
                curNode.children[index] = TrieNode()
            curNode = curNode.children[index]
        curNode.isEnd = True

    def search(self, word: str) -> bool:

        # Checks whether the substring is in the Trie rooted at root
        def dfs(substring, root):
            # Base case
            if not root:
                return False

            # Base case 2
            if len(substring) == 0:
                return root.isEnd

            char = substring[0]
            if char != ".":              
                index = ord(char) - ord("a")
                if not root.children[index]:
                    return False
                else:
                    return dfs(substring[1:], root.children[index])
            else: # Any character
                for child in root.children:
                    if dfs(substring[1:], child):
                        return True
                return False

        return dfs(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)