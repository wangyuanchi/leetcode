class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (!nums.size()) return 0;
        auto l {0uz};
        auto r {nums.size() - 1};
        while(l != r) {
            while (nums[l] != val && l != r) ++l;
            while (nums[r] == val && l != r) --r;
            std::swap(nums[l], nums[r]);
        }
        if (nums[l] == val) return l;
        return l + 1;
    }
};