class Node:

    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.num_of_buckets = 1000
        self.hm = [None] * self.num_of_buckets

    def get_bucket(self, key: int) -> int:
        return key % self.num_of_buckets

    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket(key)

        if not self.hm[bucket]:
            self.hm[bucket] = Node(key, value)
            return

        cur_node = self.hm[bucket]
        while cur_node:
            if key == cur_node.key:
                cur_node.val = value
                return
            cur_node = cur_node.next

        cur_node = Node(key, value)
        cur_node.next = self.hm[bucket]
        self.hm[bucket] = cur_node

    def get(self, key: int) -> int:
        bucket = self.get_bucket(key)

        if not self.hm[bucket]:
            return -1

        cur_node = self.hm[bucket]
        
        while cur_node:
            if key == cur_node.key:
                return cur_node.val
            cur_node = cur_node.next

        return -1
        
    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)

        if not self.hm[bucket]:
            return

        cur_node = self.hm[bucket]
        if cur_node.key == key:
            self.hm[bucket] = cur_node.next
            return

        prev = None
        while cur_node:
            if key == cur_node.key:
                prev.next = cur_node.next
                return
            prev, cur_node = cur_node, cur_node.next
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)