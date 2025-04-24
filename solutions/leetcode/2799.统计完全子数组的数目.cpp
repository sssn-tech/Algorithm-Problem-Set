/*
 * @lc app=leetcode.cn id=2799 lang=cpp
 *
 * [2799] 统计完全子数组的数目
 */

// @lc code=start
class Solution {
    public:
        int countCompleteSubarrays(vector<int>& nums) {
            int n = set<int>(nums.begin(), nums.end()).size();
    
            int lo = 0, hi = 0, ans = 0;
            map<int, int> mp;
            while (hi < nums.size()) {
                mp[nums[hi]]++;
                while (mp.size() == n) {
                    ans += nums.size() - hi;
                    mp[nums[lo]]--;
                    if (mp[nums[lo]] <= 0) 
                        mp.erase(nums[lo]);
                    lo++;
                }
                hi++;
            }
            return ans;
        }
    };
// @lc code=end

