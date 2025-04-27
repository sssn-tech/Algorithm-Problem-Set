/*
 * @lc app=leetcode.cn id=124 lang=cpp
 *
 * [124] 二叉树中的最大路径和
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
// 以某点为根的最大路径和 = 左侧最大 + 右侧最大
class Solution {
    public:
        int ans;
        int maxValue(TreeNode* root) {
            if (!root)
                return 0;
            int le = max(0, maxValue(root->left));
            int ri = max(0, maxValue(root->right));
            ans = max(ans, le + ri + root->val); // 经过
            return root->val + max(0, max(le, ri));
        }
        int maxPathSum(TreeNode* root) {
            ans = -(1<<30);
            auto _ = maxValue(root);
            return ans;
        }
    };
    
    
// @lc code=end

