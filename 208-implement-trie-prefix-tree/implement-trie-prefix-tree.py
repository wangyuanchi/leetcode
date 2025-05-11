class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for letter in word:
            letterIndex = ord(letter) - ord('a')
            if currNode.children[letterIndex]: # if letter is already added
                currNode = currNode.children[letterIndex]
            else:
                currNode.children[letterIndex] = TrieNode()
                currNode = currNode.children[letterIndex]
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for letter in word:
            letterIndex = ord(letter) - ord('a')
            if currNode.children[letterIndex]: # if letter is present
                currNode = currNode.children[letterIndex]
            else:
                return False
        return currNode.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for letter in prefix:
            letterIndex = ord(letter) - ord('a')
            if currNode.children[letterIndex]: # if letter is present
                currNode = currNode.children[letterIndex]
            else:
                return False
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)