class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate{};
        int candidateCount{};
        for (int num : nums) {
            if (candidateCount == 0) {
                candidate = num;
                ++candidateCount;
            } else {
                if (num == candidate) ++candidateCount;
                else --candidateCount;
            }
        }
        return candidate;
    }
};