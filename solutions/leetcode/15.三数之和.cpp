/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
    public:
        vector<vector<int>> threeSum(vector<int>& nums) {
            sort(nums.begin(), nums.end());
            int n = nums.size();
    
            vector<vector<int>> ans;
            for (int i = 0; i < n; i++) {
                if (i > 0 && nums[i] == nums[i - 1]) continue; // 跳过重复的 nums[i]
                int curr = nums[i];
                if (curr > 0) break;
                int l = i + 1, r = n - 1;
                while (l < n && r >= 0 && l < r) {
                    int s = nums[i] + nums[l] + nums[r];
                    if (s == 0) {
                        ans.push_back({nums[i], nums[l], nums[r]});
                        while (l < r && nums[l] == nums[l + 1]) l++;
                        while (l < r && nums[r] == nums[r - 1]) r--;
                        l++;
                        r--;
                    }
                    else if (s > 0) r--;
                    else if (s < 0) l++;
                }
            }
            return ans;
        }
    };
// @lc code=end

