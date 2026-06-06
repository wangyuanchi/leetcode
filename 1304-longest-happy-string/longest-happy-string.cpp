class Solution {
private:
    std::unordered_map<char, int> freq {};
    char prevFirst {};
    char prevSecond {};
    string res {};

    char getExcludedChar() {
        if (prevFirst == 'a' && prevSecond == 'a') return 'a';
        if (prevFirst == 'b' && prevSecond == 'b') return 'b';
        if (prevFirst == 'c' && prevSecond == 'c') return 'c';
        return '\0';
    }

    void setNextChar(char c) {
        res += c;
        swap(prevFirst, prevSecond);
        prevSecond = c;
        --freq[c];
    }

    char getNextChar() {
        char curChar {};
        int curFreq {};
        for (const auto& [c, f] : freq) {
            if (f == 0) continue;
            if (c == getExcludedChar()) continue;
            if (f > curFreq) {
                curFreq = f;
                curChar = c;
            }
        }
        return curChar;
    }

public:
    string longestDiverseString(int a, int b, int c) {
        freq['a'] = a;
        freq['b'] = b;
        freq['c'] = c;

        while (true) {
            char nextChar {getNextChar()};
            if (!nextChar) {
                break;
            }
            setNextChar(nextChar);
        }

        return res;
    }
};