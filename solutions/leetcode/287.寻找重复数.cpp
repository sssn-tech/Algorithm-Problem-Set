/*
 * @lc app=leetcode.cn id=287 lang=cpp
 *
 * [287] 寻找重复数
 */

// @lc code=start
class Solution {
    public:
        int findDuplicate(vector<int>& nums) {
            int slow = 0, fast = 0;
            while (true) {
                slow = nums[slow];
                fast = nums[nums[fast]];
                if (slow == fast) {
                    fast = 0;
                    while (slow != fast) {
                        slow = nums[slow];
                        fast = nums[fast];
                    }
                    return slow;
                }
            }
        }
    };
// @lc code=end

