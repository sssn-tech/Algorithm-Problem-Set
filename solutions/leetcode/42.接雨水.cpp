/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public:
        int trap(vector<int>& height) {
            // position i's capacity:
            // l = min(max(height[:i]), max(height[i+1:]))
            // l * (l - height[i])
            int ans = 0;
            vector<int> preifx_max; // max(height[:i])
            for (int i = 0; i < height.size(); i++) {
                if (i == 0) 
                    preifx_max.push_back(height[i]);
                else 
                    preifx_max.push_back(max(height[i], preifx_max[preifx_max.size() - 1]));
            }
            int suffix_max = -1;
            for (int i = height.size() - 2; i >= 1; i--) {
                suffix_max = max(suffix_max, height[i + 1]);
                int l = min(suffix_max, preifx_max[i - 1]);
                ans += max(0, l - height[i]);
            }
            return ans;
        }
    };
// @lc code=end

