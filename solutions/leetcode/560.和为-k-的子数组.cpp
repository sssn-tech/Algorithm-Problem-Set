/*
 * @lc app=leetcode.cn id=560 lang=cpp
 *
 * [560] 和为 K 的子数组
 */

// @lc code=start
class Solution {
    public:
        int subarraySum(vector<int>& nums, int k) {
            // 要求得所有的i, j 使得 sums[j] - sums[i - 1] = k
            // 可以枚举i, 求所有的j 满足 sums[j] = k + sums[i - 1]
            // 这样的话, 就变成了两数之和的问题
            vector<int> sums;
            map<int, int> sums_freq;
            for (int i = 0; i < nums.size(); i++) {
                if (i == 0) sums.push_back(nums[i]);
                else sums.push_back(sums[sums.size() - 1] + nums[i]);
                sums_freq[sums[sums.size() - 1]]++;
            }
    
            int ans = 0;
            for (int i = 0; i < nums.size(); i++) {
                if (sums[i] == k) ans++;
                if (i > 0)  ans += sums_freq[k + sums[i - 1]];
                sums_freq[sums[i]] -= 1;
            }
            return ans;
    
        }
    };
// @lc code=end

