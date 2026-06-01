class Solution {
public:
    void reverseString(vector<char>& s) {
        auto l {0uz};
        auto r {s.size() - 1};
        while (l < r) {
            std::swap(s[l], s[r]);
            ++l; --r;
        }
    }
};