class Node:

    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.num_of_buckets = 1000
        self.hm = []

    def get_bucket(self, key: int) -> int:
        return key % self.num_of_buckets

    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket(key)

        if not self.hm:
            self.hm.append(Node(key, value))
            return

        cur_node = self.hm[0]
        while cur_node:
            if key == cur_node.key:
                cur_node.val = value
                return
            cur_node = cur_node.next

        cur_node = Node(key, value)
        cur_node.next = self.hm[0]
        self.hm[0] = cur_node

    def get(self, key: int) -> int:
        bucket = self.get_bucket(key)

        if not self.hm:
            return -1

        cur_node = self.hm[0]
        
        while cur_node:
            if key == cur_node.key:
                return cur_node.val
            cur_node = cur_node.next

        return -1
        
    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)

        if not self.hm or not self.hm[0]:
            return

        cur_node = self.hm[0]
        if cur_node.key == key:
            self.hm[0] = cur_node.next
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