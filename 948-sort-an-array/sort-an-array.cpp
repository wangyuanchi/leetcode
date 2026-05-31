class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }
 
    void quickSort(vector<int>& nums, int l, int r) {
        if (l >= r) return;

        int p{partitionArray(nums, l, r)};

        quickSort(nums, l, p - 1);
        quickSort(nums, p + 1, r);
    }

    int partitionArray(vector<int>& nums, int l, int r) {
        int p {std::rand() % (r - l + 1) + l};
        std::swap(nums[p], nums[r]);
        for (int i{l}; i < r; ++i) {
            if (nums[i] >= nums[r]) continue;
            std::swap(nums[i], nums[l]);
            ++l;
        }
        std::swap(nums[l], nums[r]);
        return l;
    }
};