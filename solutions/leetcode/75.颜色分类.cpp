/*
 * @lc app=leetcode.cn id=75 lang=cpp
 *
 * [75] 颜色分类
 */

// @lc code=start
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int lo = 0, curr = 0, hi = nums.size() - 1;
        while (curr <= hi) {
            if (nums[curr] == 0) {
                swap(nums[curr], nums[lo]);
                curr++;
                lo++;
            } else if (nums[curr] == 2) {
                swap(nums[curr], nums[hi]);
                hi--;
            } else {
                curr++;
            }
        }
    }
};
// @lc code=end

