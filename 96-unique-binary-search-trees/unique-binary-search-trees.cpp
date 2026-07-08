class Solution {
public:
    int numTrees(int n) {
        std::vector<int> dp (n + 1);
        dp[0] = 1; // so that multiplication is not done with 0
        dp[1] = 1;

        for (int i{2}; i < dp.size(); ++i) {
            for (int j{}; j < i; ++j) {
                dp[i] += dp[j] * dp[i - 1 - j];
            }
        }
        return dp[dp.size() - 1];
    }
};