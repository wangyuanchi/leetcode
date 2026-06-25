class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        vector<int> prefix_sum {}; // subarray in here with sum > 0 is a majority subarray
        for (int i{}; i < nums.size(); ++i) {
            if (i == 0) {
                prefix_sum.push_back(nums[i] == target ? 1 : -1);
            } else {
                prefix_sum.push_back(prefix_sum[i - 1]);
                if (nums[i] == target) {
                    ++prefix_sum[i];
                } else {
                    --prefix_sum[i];
                }
            }
        }

        // Since going from prefix_sum[i] to prefix_sum[i + 1] has a max change of +- 1
        // if we know the number of majority subarrays (x) that end at i,
        // and suppose that the next value in prefix_sum is an increase,
        // then the number of majority of subarrays that end at i + 1 is x +
        // number of occurrences of prefix_sum[i + 1] - 1
        // If it is a decrease, then x - prefix_sum[i + 1]

        std::unordered_map<int, int> prefix_freq {};
        ++prefix_freq[0];

        int res {};
        int count {};

        if (prefix_sum[0] == 1) {
            ++res;
            ++count;
        }
        ++prefix_freq[prefix_sum[0]];

        for (int i{1}; i < prefix_sum.size(); ++i) {
            if (prefix_sum[i] > prefix_sum[i - 1]) {
                count += prefix_freq[prefix_sum[i - 1]];
            } else {
                count -= prefix_freq[prefix_sum[i]];
            }
            res += count;
            ++prefix_freq[prefix_sum[i]];
        }

        return res;
    }
};
