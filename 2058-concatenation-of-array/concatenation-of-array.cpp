class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> res (nums.size() * 2);
        for (int i{}; i < nums.size(); ++i) {
            res[i] = nums[i];
            res[i + nums.size()] = nums[i];
        }
        return res;
    }
};