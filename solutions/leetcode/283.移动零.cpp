/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int n = nums.size();
            if (n < 2)
                return ;
    
            int lo = 0, hi = 0; // lo找0, hi找非0
            while (lo < n && hi < n) {
                while (lo < n && nums[lo] != 0) 
                    lo++;
                hi = lo;
                while (hi < n && nums[hi] == 0) 
                    hi++;
                if (lo < n && hi < n)
                    swap(nums[lo], nums[hi]);
            }
            return ;
    
        }
    };
// @lc code=end

