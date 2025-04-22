/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
    public:
        int maxArea(vector<int>& height) {
            // initiate double pointer i and j to the start and end of 
            // the array respectively
            // if you shrink the taller bar inwards, the capacity will go down surely
            // if you shrink the shorter bar inwards, the capacity might go up or down
            int i = 0, j = height.size() - 1;
            int ans = 0;
            while (i < j) {
                ans = max(ans, min(height[i], height[j]) * (j - i));
                if (height[i] >= height[j]) {
                    j -= 1;
                } else {
                    i += 1;
                }
            }
            return ans;
        }
    };
// @lc code=end

