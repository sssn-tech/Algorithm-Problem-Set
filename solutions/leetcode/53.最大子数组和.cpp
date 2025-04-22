/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */

// @lc code=start
class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            const int INF = (1 << 30);
            int ans = -INF, pre = -INF;
            for (int i = 0; i < nums.size(); i++) {
                pre = max(pre + nums[i], nums[i]);
                ans = max(ans, pre);
            }
            return ans;
        }
    };
// @lc code=end

