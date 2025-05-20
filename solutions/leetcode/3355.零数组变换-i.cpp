/*
 * @lc app=leetcode.cn id=3355 lang=cpp
 *
 * [3355] 零数组变换 I
 */

// @lc code=start
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        // 构建查分数组
        vector<int> diff(n);
        for (int i = 0; i < n; i++) {
            diff[i] = nums[i];
            if (i > 0)
                diff[i] -= nums[i - 1];
        }
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            diff[l] -= 1;
            if (r + 1 < n)
                diff[r + 1] += 1;
        }
        // 还原出最小值数组
        int s = 0;
        for (int i = 0; i < n; i++) {
            s += diff[i];
            diff[i] = s;
            if (diff[i] > 0)
                return false;
        }
        return true;

    }
};
// @lc code=end

