class Solution {
public:
    void sortColors(vector<int>& nums) {
        int white{};
        int blue{};
        for (int i{}; i < nums.size(); ++i) {
            if (nums[i] == 2) continue;
            std::swap(nums[i], nums[blue]);
            if (nums[blue] == 0) {
                std::swap(nums [blue], nums[white]);
                ++white;
            }
            ++blue;
        }
    }
};