class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        auto m {grid.size()};
        auto n {grid[0].size()};
        auto total_slots {m * n};
        vector<vector<int>> res (m, vector<int>(n));
        for (int i{}; i < m; ++i) {
            for (int j{}; j < n; ++j) {
                auto cur_slot {i * n + j};
                auto next_slot {(cur_slot + k) % total_slots};
                res[next_slot / n][next_slot % n] = grid[i][j];
            }
        }
        return res;
    }
};