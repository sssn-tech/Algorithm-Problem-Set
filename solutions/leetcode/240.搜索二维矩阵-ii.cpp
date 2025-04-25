/*
 * @lc app=leetcode.cn id=240 lang=cpp
 *
 * [240] 搜索二维矩阵 II
 */

// @lc code=start
class Solution {
    public:
        bool searchMatrix(vector<vector<int>>& matrix, int target) {
            int n = matrix.size(), m = matrix[0].size();
            int x = 0, y = matrix[0].size() - 1;
            while (x >= 0 && x < n && y >= 0 && y < m) {
                if (matrix[x][y] == target)
                    return true;
                else if (matrix[x][y] > target)
                    y--;
                else
                    x++;
            }
            return false;
        }
    };
// @lc code=end

