class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        return k * (
            static_cast<long long>(*std::max_element(nums.begin(), nums.end())) - 
            static_cast<long long>(*std::min_element(nums.begin(), nums.end()))
        );
    }
};