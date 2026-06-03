class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stk {};
        for (auto size : asteroids) {
            if (size > 0) {
                stk.push_back(size);
                continue;
            }

            int curSize {abs(size)};
            bool curDestroyed {};
            while (stk.size() > 0 && stk.back() > 0) {
                int prevSize {abs(stk.back())};
                if (prevSize == curSize) {
                    stk.pop_back();
                    curDestroyed = true;
                    break;
                } else if (prevSize > curSize) {
                    curDestroyed = true;
                    break;
                } else {
                    stk.pop_back();
                }
            }
            
            if (!curDestroyed) stk.push_back(size);
        }
        return stk;
    }
};