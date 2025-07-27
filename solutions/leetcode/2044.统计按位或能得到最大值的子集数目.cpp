/*
 * @lc app=leetcode.cn id=2044 lang=cpp
 *
 * [2044] 统计按位或能得到最大值的子集数目
 */

// @lc code=start
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int maxOr = -1, ans = 0, n = nums.size();
        int mask = (1 << n); // 位运算枚举集合的方法
        while (--mask) {
            int res = 0;
            for (int i = 0; i < n; i++) 
                if ((mask >> i) & 1)
                    res |= nums[i];
            if (res == maxOr) 
                ans++;
            if (res > maxOr) {
                maxOr = res;
                ans = 1;
            }

        }
        return ans;
    }
};
// @lc code=end

