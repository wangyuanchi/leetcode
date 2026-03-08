class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor's diagonal argument
        n = len(nums)
        diff = ["0"] * n
        for i in range(n):
            diff[i] = "1" if nums[i][i] == "0" else "0"
        return "".join(diff)