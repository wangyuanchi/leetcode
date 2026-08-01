class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {} # key: (i, j), value: largest possible from nums[i:j+1] from pov of player 1\

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i > j:
                return 0
            
            if i == j:
                return nums[i]

            if i + 1 == j:
                return max(nums[i], nums[j])

            player1_i = nums[i] + min(dp(i + 1, j - 1), dp(i + 2, j))
            player1_j = nums[j] + min(dp(i + 1, j - 1), dp(i, j - 2))
            player1 = max(player1_i, player1_j)

            memo[(i, j)] = player1
            return player1

        player1 = dp(0, len(nums) - 1)
        player2 = sum(nums) - player1
        return player1 >= player2