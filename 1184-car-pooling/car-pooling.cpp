class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        using Pair = std::pair<int, int>;
        std::priority_queue<Pair, vector<Pair>, std::greater<Pair>> startTimings {};
        std::priority_queue<Pair, vector<Pair>, std::greater<Pair>> endTimings {};

        for (const auto& trip : trips) {
            int numPassengers {trip[0]};
            int from {trip[1]};
            int to {trip[2]};
            startTimings.push({from, numPassengers});
            endTimings.push({to, numPassengers});
        }

        int curCapacity{};
        while (startTimings.size() > 0) {
            // < so that if ==, allow passengers to alight
            if (startTimings.top().first < endTimings.top().first) {
                curCapacity += startTimings.top().second;
                startTimings.pop();
                if (curCapacity > capacity) {
                    return false;
                }
            } else {
                curCapacity -= endTimings.top().second;
                endTimings.pop();
            }
        }

        return true;
    }
};