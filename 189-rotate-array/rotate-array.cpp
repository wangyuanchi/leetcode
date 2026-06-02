class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Required: AB -> BA
        // Method: AB -> BrAr -> BA
        auto b {k % nums.size()};
        std::reverse(nums.begin(), nums.end());
        std::reverse(nums.begin(), nums.begin() + b);
        std::reverse(nums.begin() + b, nums.end());
    }
};