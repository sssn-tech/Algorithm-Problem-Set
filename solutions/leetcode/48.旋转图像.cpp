/*
 * @lc app=leetcode.cn id=48 lang=cpp
 *
 * [48] 旋转图像
 */

// @lc code=start
class Solution {
    public:
        void rotate(vector<vector<int>>& matrix) {
            int n = matrix.size();
            for (int i = 0; i < n / 2; i++)
                for (int j = i; j < n - i - 1; j++) {
                    int x1 = i, y1 = j,
                        x2 = i, y2 = n - i - 1,
                        x3 = n - i - 1, y3 = n - i - 1,
                        x4 = n - i - 1, y4 = i;
                    int b = j - i;
                    x2 += b; y3 -= b; x4 -= b;
                    swap(matrix[x1][y1], matrix[x2][y2]);
                    swap(matrix[x3][y3], matrix[x4][y4]);
                    swap(matrix[x1][y1], matrix[x3][y3]);
                }
        }
    };
// @lc code=end

