class Solution {
public:
    int numSquares(int n) {
        int base{1};
        std::vector<int> squares{};
        while (true) {
            if (base * base > n) {
                break;
            }
            squares.push_back(base * base);
            ++base;
        }

        auto memo {std::vector<std::vector<int>>(
            squares.size(), std::vector<int>(n + 1, -2)
        )};
        return dp(n, squares, 0, memo);
    }

    int dp(int n, const std::vector<int>& squares, int index,
           std::vector<std::vector<int>>& memo) {
        if (n < 0) {
            return -1;
        }
        if (n == 0) {
            return 0;
        }
        if (index == squares.size()) {
            return -1;
        }
        if (memo[index][n] != -2) {
            return memo[index][n];
        }

        int chooseCurrent{dp(n - squares[index], squares, index, memo)};
        int dontChooseCurrent{dp(n, squares, index + 1, memo)};

        int res{};
        if (chooseCurrent == -1 && dontChooseCurrent == -1) {
            res = -1;
        } else if (chooseCurrent == -1) {
            res = dontChooseCurrent;
        } else if (dontChooseCurrent == -1) {
            res = chooseCurrent + 1;
        } else {
            res = std::min(chooseCurrent + 1, dontChooseCurrent);
        }

        memo[index][n] = res;
        return res;
    }
};