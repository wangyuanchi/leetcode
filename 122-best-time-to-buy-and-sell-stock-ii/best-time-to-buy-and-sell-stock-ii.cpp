class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l{};
        int r{1};
        int profit{};
        while (r < prices.size()) {
            profit += std::max(0, prices[r] - prices[l]);
            ++l;
            ++r;
        }
        return profit;
    }
};