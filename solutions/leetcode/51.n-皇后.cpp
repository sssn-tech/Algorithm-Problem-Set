/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N 皇后
 */

// @lc code=start
class Solution {
    public:
        void dfs(int p, int n, vector<string>& curr, vector<vector<string>>& ans, vector<bool>& col, vector<bool>& dg, vector<bool>& xdg) {
            // 第p行
            if (p >= n) {
                ans.push_back(curr);
                return ;
            }
            for (int i = 0; i < n; i++) {
                if (!col[i] && !dg[p - i + n] && !xdg[p + i]) {
                    col[i] = dg[p - i + n] = xdg[p + i] = true;
                    curr[p][i] = 'Q';
                    dfs(p + 1, n, curr, ans, col, dg, xdg);
                    curr[p][i] = '.';
                    col[i] = dg[p - i + n] = xdg[p + i] = false;
                }
            }
        }
        vector<vector<string>> solveNQueens(int n) {
            vector<bool> col(n, false), dg(n << 1, false), xdg(n << 1, false);
            vector<vector<string>> ans;
            vector<string> curr(n, string(n, '.'));
            dfs(0, n, curr, ans, col, dg, xdg);
            return ans;
        }
    };
// @lc code=end

