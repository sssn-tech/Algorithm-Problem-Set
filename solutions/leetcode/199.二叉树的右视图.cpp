/*
 * @lc app=leetcode.cn id=199 lang=cpp
 *
 * [199] 二叉树的右视图
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
    vector<int> rightSideView(TreeNode* root) {
        // 层序遍历
        queue<TreeNode*> que;
        vector<int> ans;
        if (!root) 
            return ans;
        que.push(root);
        // ans.push_back(root->val);
        
        while (!que.empty()) {
            int n = que.size();
            for (int i = 0; i < n; i++) {
                auto head = que.front();
                if (!i) {
                    ans.push_back(head->val);
                }
                que.pop();
                if (head->right) {
                    que.push(head->right);
                }
                if (head->left) {
                    que.push(head->left);
                }
            }
        }

        return ans;
    }
};
// @lc code=end

