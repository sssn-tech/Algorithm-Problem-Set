/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */

// @lc code=start
class Solution {
    public:
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
            int n = matrix.size(), m = matrix[0].size();
            const int INF = 1 << 30;
            const int dx[4] = {0, 1, 0, -1}, 
                      dy[4] = {1, 0, -1, 0};
            int dr = 0, vis = 0, x = 0, y = 0;
            vector<int> ans;
            while (1) {
                ans.push_back(matrix[x][y]);
                matrix[x][y] = -INF;
                int nx = x + dx[dr], ny = y + dy[dr];
                int circ = 0;
                while (nx < 0 || ny < 0 || nx >= n || ny >= m || matrix[nx][ny] == -INF) {
                    dr = (dr + 1) % 4;
                    nx = x + dx[dr];
                    ny = y + dy[dr];
                    if (++circ >= 4)
                        return ans;
                }
                x = nx;
                y = ny;
            }
            return ans;
        }
    };
// @lc code=end

