/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        return constructWithBoundary(grid, 0, grid.size() - 1, 0, grid[0].size() - 1);
    }

    Node* constructWithBoundary(vector<vector<int>>& grid, int rt, int rb, int cl, int cr) {
        int length {rb - rt + 1};
        int halfLength {length / 2};

        // base case
        if (length == 1) {
            return new Node{static_cast<bool>(grid[rt][cl]), true};
        }

        Node* topLeft {constructWithBoundary(grid, rt, rt + halfLength - 1, cl, cl + halfLength - 1)};
        Node* topRight {constructWithBoundary(grid, rt, rt + halfLength - 1, cl + halfLength, cr)};
        Node* bottomLeft {constructWithBoundary(grid, rt + halfLength, rb, cl, cl + halfLength - 1)};
        Node* bottomRight {constructWithBoundary(grid, rt + halfLength, rb, cl + halfLength, cr)};

        if (topLeft->isLeaf && topRight->isLeaf && bottomLeft->isLeaf && bottomRight->isLeaf) {
            if ((!topLeft->val && !topRight->val && !bottomLeft->val && !bottomRight->val) ||
                (topLeft->val && topRight->val && bottomLeft->val && bottomRight->val)) {
                int v {topLeft->val};
                delete topLeft;
                delete topRight;
                delete bottomLeft;
                delete bottomRight;
                return new Node{static_cast<bool>(v), true};
            }
        }
        return new Node{true, false, topLeft, topRight, bottomLeft, bottomRight};
    }
};