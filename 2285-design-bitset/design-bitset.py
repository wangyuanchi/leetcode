class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bit_set = [0] * size
        self.bit_set_opposite = [1] * size
        self.num_of_ones = 0 # this references self.bit_set

    def fix(self, idx: int) -> None:
        if self.bit_set[idx] != 1:
            self.bit_set[idx] = 1
            self.bit_set_opposite[idx] = 0
            self.num_of_ones += 1
        

    def unfix(self, idx: int) -> None:
        if self.bit_set[idx] != 0:
            self.bit_set[idx] = 0
            self.bit_set_opposite[idx] = 1
            self.num_of_ones -= 1

    def flip(self) -> None:
        self.bit_set, self.bit_set_opposite = self.bit_set_opposite, self.bit_set
        self.num_of_ones = self.size - self.num_of_ones

    def all(self) -> bool:
        return self.size == self.num_of_ones

    def one(self) -> bool:
        return self.num_of_ones > 0

    def count(self) -> int:
        return self.num_of_ones

    def toString(self) -> str:
        res = ""
        for i in range(self.size):
            res += str(self.bit_set[i])
        return res
        
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()