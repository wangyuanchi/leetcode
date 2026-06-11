class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int sum {std::accumulate(matchsticks.begin(), matchsticks.end(), 0)};
        if (sum % 4) {
            return false;
        }
        std::array<int, 4> builder {};
        return backtrack(matchsticks, sum / 4, builder, 0);
    }

    bool backtrack(const vector<int>& matchsticks, int length, std::array<int, 4>& sides, int index) {
        if (index == matchsticks.size()) {
            return sides[0] == length && sides[1] == length && sides[2] == length && sides[3] == length;
        }

        for (int& side : sides) {
            if (side + matchsticks[index] <= length) {
                side += matchsticks[index];
                if (backtrack(matchsticks, length, sides, index + 1)) {
                    return true;
                }
                side -= matchsticks[index];
            }

            if (side == 0) {
                break;
            } // pruning, putting this matchstick in another side won't change outcome
        }

        return false;
    }
};