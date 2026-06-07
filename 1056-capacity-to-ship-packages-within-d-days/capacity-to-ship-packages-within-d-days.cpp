class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int l {*std::max_element(weights.begin(), weights.end())};
        int r {std::accumulate(weights.begin(), weights.end(), 0)};

        while (l < r) {
            int m {l + (r - l) / 2};
            if (daysToShip(weights, m) > days) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }

    int daysToShip(const vector<int>& weights, int capacity) {
        int days{};
        int curWeight {};
        for (int weight : weights) {
            if (curWeight + weight <= capacity) {
                curWeight += weight;
                continue;
            }
            curWeight = weight;
            ++days;
        }
        return ++days;
    }
};