/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) {
            return nullptr;
        }

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
            return root;
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
            return root;
        }

        // Now, we know that the root's value is equal to the key
        if (!root->left && !root->right) {
            delete root;
            return nullptr;
        }

        if (root->left && !root->right) {
            TreeNode* temp {root->left};
            delete root;
            return temp;
        }
        
        if (!root->left && root->right) {
            TreeNode* temp {root->right};
            delete root;
            return temp;
        }

        // Root has 2 children
        TreeNode* successor {root->right};
        while(successor->left) {
            successor = successor->left;
        }
        std::swap(successor->val, root->val);

        root->right = deleteNode(root->right, successor->val);
        return root;
    }
};