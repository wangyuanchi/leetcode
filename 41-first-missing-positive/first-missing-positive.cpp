class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        // The missing positive has to be between 1 and nums.size() + 1 inclusive.
        // If we had nums as a set, then we can just check values in the set.
        // Here, we let nums itself represent the set, with -ve indicating existence.

        // Set irrelevant values to 0
        for (int& num : nums) {
            // if == nums.size() + 1, res can't be it, helps with indexing
            if (num < 0 || num >= nums.size() + 1) {
                num = 0;
            }
        }

        for (int i{}; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                continue;
            }
            int val {std::abs(nums[i])};
            int index {val - 1};
            if (nums[index] == 0) {
                nums[index] = -val;
            } else if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }

        for (int i{}; i < nums.size(); ++i) {
            if (nums[i] >= 0) {
                return i + 1;
            }
        }
        return nums.size() + 1;
    }
};