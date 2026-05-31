class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        auto prefixLength {strs[0].size()};
        for (auto i{1uz}; i < strs.size(); ++i) {
            prefixLength = std::min(prefixLength, strs[i].size());
            std::size_t cur {};
            while (cur < prefixLength) {
                if (strs[0][cur] != strs[i][cur]) {
                    prefixLength = cur;
                    break;
                }
                ++cur;
            }
        }
        return strs[0].substr(0, prefixLength);
    }
};