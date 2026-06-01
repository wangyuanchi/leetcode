class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        // Assuming that number of people >> limit
        std::vector<int> buckets (limit + 1);
        for (auto weight : people) {
            ++buckets[weight];
        }
        std::vector<int> sortedPeople {};
        for (int weight{}; weight < buckets.size(); ++weight) {
            for (int i{}; i < buckets[weight]; ++i) {
                sortedPeople.push_back(weight);
            }
        }

        auto l {0uz};
        auto r {sortedPeople.size() - 1};
        int boats{};

        while (l < r) {
            if (sortedPeople[r] + sortedPeople[l] <= limit) {
                ++l;
            }
            --r;
            ++boats;
        }
        
        if (l == r) ++boats;
        return boats;
    }
};