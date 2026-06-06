class Solution {
public:
    string reorganizeString(string s) {
        std::unordered_map<char, int> freq {};
        for (const auto& c : s) {
            ++freq[c];
        }
        std::priority_queue<std::tuple<int, char>> maxHeap {};
        for (const auto& [c, f] : freq) {
            maxHeap.push({f, c});
        }
        std::tuple<int, char> prev {};
        std::string res {};

        while (maxHeap.size() > 0) {
            auto [f, c] = maxHeap.top();
            maxHeap.pop();
            res += c;
            --f;
            auto [prevF, prevC] = prev;
            if (prevF > 0) {
                maxHeap.push({prevF, prevC});
            }
            prev = {f, c};
        }

        if (res.size() == s.size()) {
            return res;
        }
        return {};
    }
};