class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.mirror = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.mirror.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1

        base_value = self.stack.pop()
        lazy_add = self.mirror.pop()

        if self.stack:
            self.mirror[-1] += lazy_add

        return base_value + lazy_add

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return

        target_index = min(k, len(self.stack)) - 1
        self.mirror[target_index] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)