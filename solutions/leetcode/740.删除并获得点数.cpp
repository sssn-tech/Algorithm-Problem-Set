/*
 * @lc app=leetcode.cn id=740 lang=cpp
 *
 * [740] 删除并获得点数
 */

// @lc code=start
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        map<int, int> mp;
        for (auto& num : nums)
            mp[num]++;
        int pre = -10, n = mp.size();
        vector<int> f(n + 10, 0);
        int i = 2, ans = -1;
        for (auto& pii : mp) {
            int num = pii.first, rep = pii.second;
            if (pre + 1 == num) {
                f[i] = max(f[i - 1], f[i - 2] + num * rep);
            } else {
                f[i] = f[i - 1] + num * rep;
            }
            pre = num;
            ans = max(ans, f[i]);
            i++;
        }
        return ans;
    }
};
// @lc code=end

