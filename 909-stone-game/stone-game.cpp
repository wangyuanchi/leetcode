class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int sum {std::accumulate(piles.begin(), piles.end(), 0)};
        auto memo {std::vector<std::vector<int>>(piles.size(), std::vector<int>(piles.size(), -1))};
        int val {dp(piles, memo, 0, piles.size() - 1)};
        return val > sum - val;
    }

    int dp(const std::vector<int>& piles, std::vector<std::vector<int>>& memo, int l, int r) {
        if (l > r) {
            return 0;
        }
        if (l == r) {
            return piles[l];
        }
        if (memo[l][r] != -1) {
            return memo[l][r];
        }
        memo[l][r] = std::max(
            piles[l] + std::min(dp(piles, memo, l + 2, r), dp(piles, memo, l + 1, r - 1)),
            piles[r] + std::min(dp(piles, memo, l, r - 2), dp(piles, memo, l + 1, r - 1))
        );
        return memo[l][r];
    }
};