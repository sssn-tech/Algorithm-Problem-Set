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
    private:
        void dfs(TreeNode* root, vector<long long>& prefix_sum, int& ans, const int& targetSum) {
            if (!root)
                return ;
            long long prefix = prefix_sum[prefix_sum.size() - 1]; // 至少有一个0, 不用判空
            prefix_sum.push_back(prefix + root->val);
            
            // cout << root->val << ':';
            // for (auto& num: prefix_sum) 
            //     cout << num << ' ';
            // cout << endl;
            
            int n = prefix_sum.size();
            long long last = prefix + root->val;
            for (int i = 0; i < n - 1; i++) {
                if (last - prefix_sum[i] == targetSum)
                    ans++;
            }
    
            dfs(root->left, prefix_sum, ans, targetSum);
            dfs(root->right, prefix_sum, ans, targetSum);
            prefix_sum.pop_back();
    
        }
    public:
        int pathSum(TreeNode* root, int targetSum) {
            int ans = 0;
            vector<long long> prefix_sum = vector<long long>({0});
            dfs(root, prefix_sum, ans, targetSum);
            return ans;
        }
    };