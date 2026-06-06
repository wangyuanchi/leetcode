class Solution {
    vector<vector<int>> res {};
    vector<int> builder {};

public:
    vector<vector<int>> combine(int n, int k) {
        dfs(1, n, k);
        return res;
    }

    void dfs(int val, int n, int k) {
        // base case
        if (builder.size() == k) {
            res.push_back(builder); // deep copy
            return;
        }

        if (val == n + 1) {
            return;
        }

        // pruning
        int maxRemaining {n - val + 1};
        if (k - builder.size() > maxRemaining) {
            return;
        }

        // we choose val
        builder.push_back(val);
        dfs(val + 1, n, k);

        // we don't choose val
        builder.pop_back();
        dfs(val + 1, n, k);
    }
};