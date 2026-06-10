struct TrieNode {
    std::array<TrieNode*, 26> children {};
    bool isEnd {};

    void insertWord(std::string_view word) {
        TrieNode* curNode {this};
        for (char c : word) {
            int index {c - 'a'};
            if (!curNode->children[index]) {
                curNode->children[index] = new TrieNode{};
            }
            curNode = curNode->children[index];
        }
        curNode->isEnd = true;
    }

    // returns a set of end indexes such that each substr in s
    // from start index to end index inclusive is in the Trie
    std::unordered_set<int> findWords(std::string_view s, int startIndex) {
        TrieNode* curNode {this};
        std::unordered_set<int> endIndexes {};
        for (int i{startIndex}; i < s.size(); ++i) {
            int childIndex {s[i] - 'a'};
            if (!curNode->children[childIndex]) {
                return endIndexes;
            }
            
            curNode = curNode->children[childIndex];
            if (curNode->isEnd) {
                endIndexes.insert(i);
            }
        }
        return endIndexes;
    }
};

class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        TrieNode* root {new TrieNode{}};
        for (const auto& word : dictionary) {
            root->insertWord(word);
        }
        std::unordered_map<int, int> memo {};
        return dp(s, root, memo, 0);
    }

    // dp for s.substr(index)
    int dp(std::string_view s, TrieNode* root, std::unordered_map<int, int>& memo, int index) {
        if (memo.contains(index)) {
            return memo[index];
        }

        if (index >= s.size()) {
            return 0;
        }

        std::unordered_set<int> endIndexes {root->findWords(s, index)};
        int minCharacters = s.size() - index + 1;
        for (int endIndex{index}; endIndex < s.size(); ++endIndex) {
            if (endIndexes.contains(endIndex)) {
                minCharacters = std::min(minCharacters, dp(s, root, memo, endIndex + 1));
            } else {
                minCharacters = std::min(
                    minCharacters, endIndex - index + 1 + dp(s, root, memo, endIndex + 1)
                );
            }
        }
        memo[index] = minCharacters;

        return minCharacters;
    }
};