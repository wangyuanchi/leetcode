class Node:
    def __init__(self, key: int, val: int, prev: "Node" = None, next: "Node" = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # k is key, v is pointer to Node
        self.totalCapacity = capacity
        self.currentCapacity = 0
        self.tail = Node(0, 0, None, None) # dummy, least recently used
        self.head = Node(0, 0, None, None) # dummy, most recently used
        self.tail.next, self.head.prev = self.head, self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            self.used(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.used(key)
        else:
            newNode = Node(key, value, self.head.prev, self.head)
            self.cache[key] = newNode
            self.head.prev.next = newNode
            self.head.prev = newNode
            self.currentCapacity += 1
            if (self.currentCapacity > self.totalCapacity):
                self.deleteLRU()

    def deleteLRU(self) -> None:
        LRU = self.tail.next
        del self.cache[LRU.key]
        self.tail.next = LRU.next
        LRU.next.prev = self.tail

    def used(self, key: int) -> None:
        curNode = self.cache[key]
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev
        curNode.next = self.head
        curNode.prev = self.head.prev
        self.head.prev.next = curNode
        self.head.prev = curNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)