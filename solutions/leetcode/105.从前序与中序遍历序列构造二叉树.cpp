/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
 */

// @lc code=start
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = preorder.size();
        if (!n) 
            return nullptr;
        if (n == 1)
            return new TreeNode(preorder[0]);
        int root_val = preorder[0];
        auto root_it = find(inorder.begin(), inorder.end(), root_val);
        int root_pos = root_it - inorder.begin();

        vector<int> le_preorder = vector<int>(preorder.begin() + 1, preorder.begin() + 1 + root_pos);
        vector<int> ri_preorder = vector<int>(preorder.begin() + 1 + root_pos, preorder.end());

        vector<int> le_inorder = vector<int>(inorder.begin(), inorder.begin() + root_pos);
        vector<int> ri_inorder = vector<int>(inorder.begin() + root_pos + 1, inorder.end());

        TreeNode *le_tree = buildTree(le_preorder, le_inorder);
        TreeNode *ri_tree = buildTree(ri_preorder, ri_inorder);

        return new TreeNode(root_val, le_tree, ri_tree);

    }
};
// @lc code=end

