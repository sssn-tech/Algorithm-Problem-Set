/*
 * @lc app=leetcode.cn id=238 lang=cpp
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int n = nums.size();
            if (n < 2)
                return nums;
            vector<int> prefix_multi;
            int temp = 1;
            for (int i = 0; i < n; i++) {
                temp *= nums[i];
                prefix_multi.push_back(temp);
            }
            int suffix = 1;
            for (int i = n - 1; i >= 0; i--) {
                suffix *= (i == n - 1 ? 1 : nums[i + 1]);
                int prefix = (i == 0 ? 1 : prefix_multi[i - 1]);
                prefix_multi[i] = suffix * prefix;
            }
            return prefix_multi;
        }
    };
// @lc code=end

